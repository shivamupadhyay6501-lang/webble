class AnswerResponse {
  final String answer;
  final List<Source> sources;

  AnswerResponse({
    required this.answer,
    required this.sources,
  });

  factory AnswerResponse.fromJson(Map<String, dynamic> json) {
    return AnswerResponse(
      answer: json['answer'] ?? '',
      sources: (json['sources'] as List<dynamic>?)
              ?.map((s) => Source.fromJson(s as Map<String, dynamic>))
              .toList() ??
          [],
    );
  }
}

class Source {
  final String title;
  final String url;
  final String snippet;

  Source({
    required this.title,
    required this.url,
    required this.snippet,
  });

  factory Source.fromJson(Map<String, dynamic> json) {
    return Source(
      title: json['title'] ?? '',
      url: json['url'] ?? '',
      snippet: json['snippet'] ?? '',
    );
  }
}
