class AppConfig {
  // Your deployed backend URL
  static const String apiBaseUrl = String.fromEnvironment(
    'API_URL',
    defaultValue: 'https://webble-production.up.railway.app', // Production
  );
  
  // For production build, use:
  // flutter build apk --dart-define=API_URL=https://your-backend.deta.app
  
  static const String appName = 'Webble';
  static const String appVersion = '1.0.0';
  
  // CHANGE THESE
  static const String supportEmail = 'support@webble.app';
  static const String privacyPolicyUrl = 'https://yourwebsite.com/privacy';
  static const String termsOfServiceUrl = 'https://yourwebsite.com/terms';
  
  // API Configuration
  static const Duration apiTimeout = Duration(seconds: 30);
  static const int maxRetries = 3;
}
