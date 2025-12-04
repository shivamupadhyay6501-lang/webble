# Deploy to Render.com - 5 Minutes

Render is more reliable than Railway. Let's deploy there.

## Step 1: Push Code to GitHub (2 minutes)

```powershell
# Initialize git if not done
git init
git add .
git commit -m "Webble backend"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/webble.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy on Render (3 minutes)

1. Go to https://render.com
2. Sign up with GitHub or email
3. Click **"New +"** > **"Web Service"**
4. Click **"Build and deploy from a Git repository"**
5. Connect your GitHub account
6. Select your **webble** repository
7. Configure:
   - **Name**: `webble-api`
   - **Region**: Choose closest to you
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
8. Click **"Advanced"**
9. Add Environment Variable:
   - **Key**: `HUGGINGFACE_API_KEY`
   - **Value**: `YOUR_HUGGINGFACE_TOKEN_HERE`
10. Click **"Create Web Service"**

## Step 3: Wait for Deployment (2-3 minutes)

Render will:
- Clone your repo
- Install dependencies
- Start your server
- Give you a URL like: `https://webble-api.onrender.com`

## Step 4: Test Your Backend

Once deployed, test it:

```powershell
$url = "https://webble-api.onrender.com"  # Replace with your actual URL
Invoke-WebRequest -Uri "$url"
```

You should see: `{"message":"Webble API - Free AI Web Search Assistant"}`

## Step 5: Update Flutter App

Edit `frontend/lib/config/app_config.dart`:

```dart
defaultValue: 'https://webble-api.onrender.com',  // Your Render URL
```

## Step 6: Rebuild App

```powershell
cd frontend
C:\flutter\bin\flutter.bat run
```

## Done!

Your backend is now on Render with a working URL!

---

## Alternative: Deploy Without GitHub

If you don't want to use GitHub:

### Option 1: Use Render's Git URL

1. Create a public repo on GitHub (even empty)
2. Push your code
3. Use the repo URL in Render

### Option 2: Use PythonAnywhere

1. Go to https://www.pythonanywhere.com
2. Sign up (free)
3. Upload your `backend` folder
4. Create a web app
5. Configure WSGI file
6. Set environment variable

---

## Render vs Railway

| Feature | Render | Railway |
|---------|--------|---------|
| Free Tier | 750 hrs/mo | 500 hrs/mo |
| Reliability | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| DNS Issues | Rare | Common |
| Setup | Web UI | CLI or Web |
| Speed | Medium | Fast |

**Recommendation**: Use Render for production apps!

---

## Need Help?

Just follow the steps above. Render's web interface is very straightforward!
