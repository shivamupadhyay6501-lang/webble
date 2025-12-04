# Deploy to Railway.app - Easiest Method (5 Minutes)

## Why Railway?
- ✅ No CLI installation needed
- ✅ Free tier (500 hours/month)
- ✅ Deploy directly from your computer
- ✅ Simple web interface
- ✅ Automatic HTTPS

## Step-by-Step Guide

### Step 1: Create GitHub Repo (2 minutes)

First, push your code to GitHub:

```powershell
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit - Webble app"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/webble.git
git branch -M main
git push -u origin main
```

**OR** if you don't want to use GitHub, skip to "Alternative: Deploy Without GitHub" below.

### Step 2: Sign Up for Railway (1 minute)

1. Go to https://railway.app
2. Click "Login" or "Start a New Project"
3. Sign up with GitHub (recommended) or email
4. Verify your email if needed

### Step 3: Deploy Your Backend (2 minutes)

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Authorize Railway to access your repos
4. Select your **webble** repository
5. Railway will detect it's a Python app automatically

### Step 4: Configure Settings

After deployment starts, click on your service, then:

1. Go to **"Settings"** tab
2. Set **Root Directory**: `backend`
3. Go to **"Variables"** tab
4. Click **"New Variable"**
   - Key: `HUGGINGFACE_API_KEY`
   - Value: `YOUR_HUGGINGFACE_TOKEN_HERE`
5. Click **"Add"**

### Step 5: Get Your URL

1. Go to **"Settings"** tab
2. Scroll to **"Networking"**
3. Click **"Generate Domain"**
4. Copy your URL (like `https://webble-production.up.railway.app`)

### Step 6: Test Your Backend

```powershell
$url = "https://your-railway-url.up.railway.app"  # Replace with your actual URL
$body = @{question="What is AI?"} | ConvertTo-Json
Invoke-WebRequest -Uri "$url/ask" -Method POST -ContentType "application/json" -Body $body
```

If you get a 200 response, it's working! 🎉

---

## Alternative: Deploy Without GitHub (Even Easier!)

If you don't want to use GitHub, use **Railway CLI**:

### Install Railway CLI

```powershell
npm install -g @railway/cli
```

**Don't have npm?** Download Node.js from https://nodejs.org (takes 2 minutes)

### Deploy

```powershell
# Login
railway login

# Link project
cd backend
railway init

# Deploy
railway up

# Set environment variable
railway variables --set HUGGINGFACE_API_KEY=YOUR_HUGGINGFACE_TOKEN_HERE

# Get URL
railway domain
```

---

## Alternative 2: Render.com (Also Easy, No GitHub Required)

### Step 1: Sign Up
1. Go to https://render.com
2. Sign up with email or GitHub

### Step 2: Create Web Service
1. Click **"New +"** > **"Web Service"**
2. Choose **"Build and deploy from a Git repository"**
3. Connect your GitHub repo OR use "Public Git repository" with your repo URL

### Step 3: Configure
- **Name**: webble-api
- **Root Directory**: `backend`
- **Runtime**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 4: Add Environment Variable
- Click **"Environment"**
- Add variable:
  - Key: `HUGGINGFACE_API_KEY`
  - Value: `YOUR_HUGGINGFACE_TOKEN_HERE`

### Step 5: Deploy
- Click **"Create Web Service"**
- Wait 2-3 minutes for deployment
- Copy your URL (like `https://webble.onrender.com`)

---

## Alternative 3: PythonAnywhere (No Git Needed!)

### Step 1: Sign Up
1. Go to https://www.pythonanywhere.com
2. Create free account

### Step 2: Upload Code
1. Go to **"Files"** tab
2. Upload your `backend` folder
3. Or use **"Bash console"** to clone from GitHub

### Step 3: Create Web App
1. Go to **"Web"** tab
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **Python 3.10**

### Step 4: Configure WSGI
1. Edit WSGI configuration file
2. Replace content with:

```python
import sys
path = '/home/YOUR_USERNAME/backend'
if path not in sys.path:
    sys.path.append(path)

from main import app as application
```

### Step 5: Install Dependencies
Open Bash console:
```bash
cd backend
pip install --user -r requirements.txt
```

### Step 6: Set Environment Variable
In Bash console:
```bash
echo 'export HUGGINGFACE_API_KEY="YOUR_HUGGINGFACE_TOKEN_HERE"' >> ~/.bashrc
source ~/.bashrc
```

### Step 7: Reload
- Go back to **"Web"** tab
- Click **"Reload"**
- Your URL: `https://YOUR_USERNAME.pythonanywhere.com`

---

## Recommended: Railway.app

**Railway is the easiest** because:
- Simple web interface
- Automatic detection of Python apps
- Free tier is generous
- Fast deployment
- Automatic HTTPS

## After Deployment

Once you have your URL, update Flutter app:

1. Edit `frontend/lib/config/app_config.dart`:
```dart
defaultValue: 'https://your-railway-url.up.railway.app',
```

2. Rebuild app:
```powershell
cd frontend
C:\flutter\bin\flutter.bat run
```

## Need Help?

Tell me which platform you want to use and I'll help you through it!
