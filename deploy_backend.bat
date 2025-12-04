@echo off
echo ========================================
echo Webble Backend Deployment Script
echo ========================================
echo.

echo Step 1: Installing Deta Space CLI...
echo.
powershell -Command "iwr https://get.deta.dev/space-cli.ps1 -useb | iex"

echo.
echo Step 2: Login to Deta Space...
echo (This will open your browser)
echo.
space login

echo.
echo Step 3: Creating new Deta Space project...
echo.
cd backend
space new

echo.
echo Step 4: Deploying your backend...
echo.
space push

echo.
echo Step 5: Setting HuggingFace API token...
echo.
space env add HUGGINGFACE_API_KEY YOUR_HUGGINGFACE_TOKEN_HERE

echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Your backend is now live!
echo Copy the URL shown above and update it in:
echo frontend\lib\config\app_config.dart
echo.
echo Then rebuild your app:
echo   cd frontend
echo   flutter run
echo.

pause
