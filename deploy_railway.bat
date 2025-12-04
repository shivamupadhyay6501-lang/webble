@echo off
echo ========================================
echo Deploying Webble to Railway.app
echo ========================================
echo.

echo Step 1: Login to Railway...
echo (This will open your browser)
echo.
railway login

echo.
echo Step 2: Initialize Railway project...
echo.
cd backend
railway init

echo.
echo Step 3: Deploying your backend...
echo (This may take 2-3 minutes)
echo.
railway up

echo.
echo Step 4: Setting environment variable...
echo.
railway variables --set HUGGINGFACE_API_KEY=YOUR_HUGGINGFACE_TOKEN_HERE

echo.
echo Step 5: Generating public URL...
echo.
railway domain

echo.
echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Copy the URL shown above and update it in:
echo frontend\lib\config\app_config.dart
echo.
echo Then test your backend:
echo   Invoke-WebRequest -Uri "https://your-url/ask" -Method POST -ContentType "application/json" -Body '{\"question\":\"test\"}'
echo.
echo Then rebuild your app:
echo   cd frontend
echo   flutter run
echo.

pause
