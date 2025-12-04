@echo off
echo Building Webble APK...
echo.

cd frontend
flutter clean
flutter pub get
flutter build apk --release --dart-define=API_URL=http://localhost:8001

echo.
echo ========================================
echo APK built successfully!
echo Location: frontend\build\app\outputs\flutter-apk\app-release.apk
echo ========================================
echo.

pause
