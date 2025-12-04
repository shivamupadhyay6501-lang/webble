# Deploy to Render.com - 5 Minutes (No CLI Needed!)

## Step 1: Sign Up (1 minute)

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with GitHub or email

## Step 2: Create Web Service (2 minutes)

1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Choose **"Build and deploy from a Git repository"**
4. Click **"Connect account"** to connect GitHub

## Step 3: Push Code to GitHub (if not done)

```powershell
cd C:\Projects\webble
git init
git add .
git commit -m "Webble app"
```

Then create a repo on GitHub and push:
```powershell
git remote add origin https://github.com/YOUR_USERNAME/webble.git
git branch -M main
git push -u origin main
```

## Step 4: Configure Render

After connecting your repo:

**Basic Settings:**
- **Name**: `webble-api`
- **Root Directory**: `backend`
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main`

**Build & Deploy:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## Step 5: Add Environment Variable

Scroll down to **"Environment Variables"**:
- Click **"Add Environment Variable"**
- **Key**: `HUGGINGFACE_API_KEY`
- **Value**: `YOUR_HUGGINGFACE_TOKEN_HERE`
- Click **"Add"**

## Step 6: Deploy!

1. Click **"Create Web Service"** at the bottom
2. Wait 2-3 minutes for deployment
3. You'll get a URL like: `https://webble-api.onrender.com`

## Step 7: Test Your Backend

Once deployed, test it:
```powershell
Invoke-WebRequest https://webble-api.onrender.com
```

Should return: `{"message":"Webble API - Free AI Web Search Assistant"}`

## Step 8: Update Flutter App

Edit `frontend/lib/config/app_config.dart`:
```dart
defaultValue: 'https://webble-api.onrender.com',  // Your Render URL
```

## Step 9: Rebuild App

```powershell
cd frontend
C:\flutter\bin\flutter.bat run
```

## Done!

Your backend is now live on Render with:
- ✅ Free tier (750 hours/month)
- ✅ Automatic HTTPS
- ✅ Auto-deploy on git push
- ✅ Easy monitoring dashboard

---

## Alternative: Deploy Without GitHub

If you don't want to use GitHub:

1. Go to Render dashboard
2. New + > Web Service
3. Select **"Deploy an existing image from a registry"**
4. Or use **"Public Git repository"** with any public repo URL

---

## Render Free Tier

- 750 hours/month free
- Spins down after 15 min of inactivity
- First request after sleep takes ~30 seconds
- Perfect for testing and low-traffic apps

---

## Need Help?

Just go to https://render.com and follow the visual interface. It's much easier than Railway CLI!
