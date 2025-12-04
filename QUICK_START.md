# Quick Start - Get Webble Running in 5 Minutes

## What You Need

1. **HuggingFace Token** (Free)
   - Go to: https://huggingface.co/settings/tokens
   - Click "New token"
   - Name it "webble"
   - Select "Read" access
   - Copy the token (starts with `hf_`)

2. **Backend URL** (After deployment)
   - Will look like: `https://webble-1-x1234567.deta.app`

## Step 1: Deploy Backend (5 minutes)

### Option A: Deta Space (Recommended - 100% Free)

```bash
# Install Deta CLI (Windows)
iwr https://get.deta.dev/space-cli.ps1 -useb | iex

# Login
space login

# Deploy
cd backend
space new
space push

# Set your HuggingFace token
space env add HUGGINGFACE_API_KEY hf_your_token_here
```

You'll get a URL like: `https://webble-1-x1234567.deta.app`

### Option B: Railway (Free tier)

1. Go to https://railway.app
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Connect your repo
5. Set root directory to `backend`
6. Add environment variable: `HUGGINGFACE_API_KEY=hf_your_token`
7. Deploy!

### Option C: Render (Free tier)

1. Go to https://render.com
2. New > Web Service
3. Connect repo
4. Root directory: `backend`
5. Build: `pip install -r requirements.txt`
6. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Add env var: `HUGGINGFACE_API_KEY`

## Step 2: Configure Flutter App

Edit `frontend/lib/config/app_config.dart`:

```dart
static const String apiBaseUrl = String.fromEnvironment(
  'API_URL',
  defaultValue: 'https://YOUR-BACKEND-URL-HERE.deta.app', // <-- CHANGE THIS
);
```

## Step 3: Run the App

```bash
cd frontend
flutter pub get
flutter run
```

## Step 4: Build for Play Store

```bash
# Build release AAB
flutter build appbundle --dart-define=API_URL=https://your-backend.deta.app

# Output location:
# build/app/outputs/bundle/release/app-release.aab
```

## Verify Everything Works

### Test Backend
```bash
curl -X POST https://your-backend.deta.app/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is AI?"}'
```

Should return JSON with answer and sources.

### Test App
1. Open app
2. Type: "What is artificial intelligence?"
3. Click "Ask"
4. Should see answer + sources in ~5-10 seconds

## Troubleshooting

### Backend returns 503
- HuggingFace model is loading (first request)
- Wait 30 seconds and try again
- App will still show search results

### "No internet connection"
- Check your backend URL in `app_config.dart`
- Make sure backend is deployed and running
- Test backend URL in browser

### Build errors
```bash
flutter clean
flutter pub get
flutter build apk --release
```

## What's Next?

1. **Customize branding** - Change app name, colors, icon
2. **Add features** - Voice input, history, favorites
3. **Improve UI** - Better animations, dark mode
4. **Deploy to Play Store** - Follow PLAY_STORE_SETUP.md

## Free Tier Limits

- **Deta Space**: Unlimited requests, 512MB RAM
- **HuggingFace**: ~30k chars/month free
- **DuckDuckGo**: No official limit (be reasonable)

If you hit limits, the app gracefully falls back to showing raw search results.
