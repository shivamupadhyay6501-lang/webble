import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import '../models/answer_response.dart';
import '../config/app_config.dart';

class ApiService {
  final http.Client _client;
  
  ApiService({http.Client? client}) : _client = client ?? http.Client();

  Future<AnswerResponse> askQuestion(String question) async {
    int retries = 0;
    
    while (retries < AppConfig.maxRetries) {
      try {
        final response = await _client
            .post(
              Uri.parse('${AppConfig.apiBaseUrl}/ask'),
              headers: {'Content-Type': 'application/json'},
              body: jsonEncode({'question': question}),
            )
            .timeout(AppConfig.apiTimeout);

        if (response.statusCode == 200) {
          final data = jsonDecode(response.body);
          return AnswerResponse.fromJson(data);
        } else if (response.statusCode >= 500 && retries < AppConfig.maxRetries - 1) {
          retries++;
          await Future.delayed(Duration(seconds: retries * 2));
          continue;
        } else {
          throw ApiException(
            'Server error: ${response.statusCode}',
            statusCode: response.statusCode,
          );
        }
      } on SocketException {
        throw ApiException(
          'No internet connection. Please check your network.',
          isNetworkError: true,
        );
      } on http.ClientException {
        throw ApiException(
          'Failed to connect to server. Please try again.',
          isNetworkError: true,
        );
      } catch (e) {
        if (retries < AppConfig.maxRetries - 1) {
          retries++;
          await Future.delayed(Duration(seconds: retries * 2));
          continue;
        }
        throw ApiException('Unexpected error: ${e.toString()}');
      }
    }
    
    throw ApiException('Failed after ${AppConfig.maxRetries} attempts');
  }

  Future<bool> checkHealth() async {
    try {
      final response = await _client
          .get(Uri.parse('${AppConfig.apiBaseUrl}/'))
          .timeout(const Duration(seconds: 5));
      return response.statusCode == 200;
    } catch (e) {
      return false;
    }
  }

  void dispose() {
    _client.close();
  }
}

class ApiException implements Exception {
  final String message;
  final int? statusCode;
  final bool isNetworkError;

  ApiException(
    this.message, {
    this.statusCode,
    this.isNetworkError = false,
  });

  @override
  String toString() => message;
}
