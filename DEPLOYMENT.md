# Webble Deployment Guide

## Prerequisites

1. **HuggingFace Account** (Free)
   - Sign up at https://huggingface.co
   - Get API token: https://huggingface.co/settings/tokens
   - Create a "Read" token (free tier)

2. **Deta Space Account** (Free)
   - Sign up at https://deta.space

## Step 1: Setup Backend Locally

```bash
cd backend
pip install -r requirements.txt
```

Create `.env` file:
```
HUGGINGFACE_API_KEY=hf_your_token_here
PORT=8000
```

Test locally:
```bash
python main.py
```

Visit: http://localhost:8000

## Step 2: Deploy to Deta Space

### Install Deta Space CLI

**Windows:**
```powershell
iwr https://get.deta.dev/space-cli.ps1 -useb | iex
```

**Mac/Linux:**
```bash
curl -fsSL https://get.deta.dev/space-cli.sh | sh
```

### Deploy

```bash
cd backend
space login
space new
space push
```

After deployment, Deta will give you a URL like:
`https://your-app-name-1-x1234567.deta.app`

### Set Environment Variables on Deta

```bash
space env add HUGGINGFACE_API_KEY hf_your_token_here
```

## Step 3: Setup Flutter Frontend

Update `frontend/lib/services/api_service.dart`:

Change:
```dart
static const String baseUrl = 'http://localhost:8000';
```

To your Deta Space URL:
```dart
static const String baseUrl = 'https://your-app-name-1-x1234567.deta.app';
```

## Step 4: Run Flutter App

```bash
cd frontend
flutter pub get
flutter run
```

For web:
```bash
flutter run -d chrome
```

For mobile:
```bash
flutter run -d android
# or
flutter run -d ios
```

## Testing the API

Test with curl:
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is artificial intelligence?"}'
```

## Troubleshooting

### HuggingFace Model Loading
If you get 503 errors, the model is loading. Wait 20-30 seconds and try again.

### CORS Issues
The backend already has CORS enabled for all origins. If issues persist, check browser console.

### DuckDuckGo Rate Limiting
DuckDuckGo API is free but may rate limit. Add delays between requests if needed.

## Free Tier Limits

- **HuggingFace**: ~30,000 characters/month free
- **Deta Space**: Unlimited requests, 512MB RAM
- **DuckDuckGo**: No official limit, but be reasonable

## Alternative Free AI Models

If Mixtral is slow, try these in `backend/main.py`:

```python
# Faster but less capable
HUGGINGFACE_MODEL = "google/flan-t5-large"

# Good balance
HUGGINGFACE_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
```
