# How to Run Webble

## Your Flutter Installation

Flutter is installed but not in your current PowerShell PATH. Here are your options:

## Option 1: Use Batch Files (Easiest)

I've created helper scripts for you:

### Run the App
Double-click: `run_app.bat`

Or in terminal:
```cmd
run_app.bat
```

### Build APK
Double-click: `build_apk.bat`

Or in terminal:
```cmd
build_apk.bat
```

## Option 2: Add Flutter to PATH

Find your Flutter installation (usually in one of these locations):
- `C:\flutter\bin`
- `C:\src\flutter\bin`
- `%USERPROFILE%\flutter\bin`

Then add to PATH:
1. Press Win + X, select "System"
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "User variables", select "Path"
5. Click "Edit" > "New"
6. Add your Flutter bin path
7. Click OK
8. **Restart PowerShell**

## Option 3: Use Full Path

If you know where Flutter is installed:

```powershell
cd frontend
C:\flutter\bin\flutter.bat pub get
C:\flutter\bin\flutter.bat run
```

## Option 4: Use CMD Instead of PowerShell

Open Command Prompt (cmd.exe) instead:

```cmd
cd frontend
flutter pub get
flutter run
```

## Option 5: Use Android Studio

1. Open Android Studio
2. File > Open > Select `frontend` folder
3. Wait for indexing
4. Click Run button (green play icon)

## Quick Test

Try this to find Flutter:

```powershell
# PowerShell
Get-Command flutter -ErrorAction SilentlyContinue

# Or search for it
Get-ChildItem C:\ -Filter flutter.bat -Recurse -ErrorAction SilentlyContinue | Select-Object FullName
```

## Current Status

✅ Backend running on http://localhost:8001
✅ Flutter installed on your system
⚠️ Flutter not in current PowerShell PATH
✅ Batch files created for easy running

## Recommended: Use the Batch Files

The easiest way right now is to just double-click:
- `run_app.bat` - to run the app
- `build_apk.bat` - to build release APK

These will work regardless of PATH issues!

## Building for Play Store

Once you're ready to build for Play Store:

1. Deploy backend to Deta Space
2. Get your production URL
3. Edit `build_apk.bat` and change:
   ```
   --dart-define=API_URL=https://your-backend.deta.app
   ```
4. Run `build_apk.bat`
5. APK will be in `frontend\build\app\outputs\flutter-apk\app-release.apk`

## Need Help?

If batch files don't work, try:
1. Restart your computer (to refresh PATH)
2. Open a new PowerShell window
3. Try `flutter --version` again
