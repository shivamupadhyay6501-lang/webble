# 🚀 Deploy Your Backend - Choose Your Method

## ✅ Recommended: Railway.app (Easiest)

I've installed Railway CLI for you. Just run:

### Option 1: Use the Batch File
Double-click: **`deploy_railway.bat`**

### Option 2: Manual Commands
```powershell
# Login (opens browser)
railway login

# Deploy
cd backend
railway init
railway up

# Set your token
railway variables --set HUGGINGFACE_API_KEY=YOUR_HUGGINGFACE_TOKEN_HERE

# Get your URL
railway domain
```

That's it! You'll get a URL like: `https://webble-production.up.railway.app`

---

## Alternative: Use Railway Website (No CLI)

If the CLI doesn't work, use the website:

1. Go to https://railway.app
2. Sign up with GitHub or email
3. Click "New Project" > "Empty Project"
4. Click "Deploy from GitHub repo" OR "Empty Service"
5. If using GitHub:
   - Connect your repo
   - Set root directory: `backend`
6. If using Empty Service:
   - Click on the service
   - Go to Settings > Source
   - Connect GitHub or upload files
7. Add environment variable:
   - Go to Variables tab
   - Add: `HUGGINGFACE_API_KEY` = `YOUR_HUGGINGFACE_TOKEN_HERE`
8. Go to Settings > Networking
9. Click "Generate Domain"
10. Copy your URL!

---

## Alternative: Render.com (Also Easy)

1. Go to https://render.com
2. Sign up
3. New > Web Service
4. Connect GitHub repo OR use public repo
5. Settings:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add environment variable:
   - `HUGGINGFACE_API_KEY` = `YOUR_HUGGINGFACE_TOKEN_HERE`
7. Click "Create Web Service"
8. Wait 2-3 minutes
9. Copy your URL!

---

## Alternative: Fly.io (Free Tier)

```powershell
# Install Fly CLI
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

# Login
fly auth login

# Deploy
cd backend
fly launch
fly secrets set HUGGINGFACE_API_KEY=YOUR_HUGGINGFACE_TOKEN_HERE
fly deploy
```

---

## What to Do After Deployment

### 1. Test Your Backend

```powershell
$url = "https://your-deployed-url.com"  # Replace with your actual URL
$body = @{question="What is AI?"} | ConvertTo-Json
Invoke-WebRequest -Uri "$url/ask" -Method POST -ContentType "application/json" -Body $body
```

You should get a 200 response with an answer!

### 2. Update Flutter App

Edit `frontend/lib/config/app_config.dart`:

```dart
static const String apiBaseUrl = String.fromEnvironment(
  'API_URL',
  defaultValue: 'https://your-deployed-url.com',  // <-- Change this
);
```

### 3. Rebuild and Test

```powershell
cd frontend
C:\flutter\bin\flutter.bat run
```

Now your app will work from anywhere, not just on your local network!

---

## Troubleshooting

### Railway CLI not working?
Use the Railway website instead (see above)

### Deployment failed?
Check the logs:
```powershell
railway logs
```

### Can't access the URL?
Make sure:
- Deployment finished successfully
- Environment variable is set
- URL includes `https://` not `http://`

---

## Quick Comparison

| Platform | Ease | Free Tier | Speed |
|----------|------|-----------|-------|
| Railway | ⭐⭐⭐⭐⭐ | 500 hrs/mo | Fast |
| Render | ⭐⭐⭐⭐ | 750 hrs/mo | Medium |
| Fly.io | ⭐⭐⭐ | 3 apps free | Fast |
| PythonAnywhere | ⭐⭐⭐ | Limited | Slow |

**Recommendation**: Use Railway - it's the easiest and fastest!

---

## Need Help?

Just run `deploy_railway.bat` and follow the prompts. If you get stuck, tell me the error message!
