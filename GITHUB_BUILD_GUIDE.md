# Build Webble APK Using GitHub Actions (No Flutter Install Needed!)

## Why This is Awesome

✅ **No Flutter installation required** on your computer
✅ **Free** - GitHub Actions is free for public repos
✅ **Automatic** - Just push code, get APK
✅ **Professional** - Same method used by big companies

## Step-by-Step Guide

### 1. Create GitHub Repository

Go to https://github.com/new and create a new repository named `webble`

### 2. Push Your Code

```bash
# In your webble folder (C:\Projects\webble)
git init
git add .
git commit -m "Initial commit - Webble AI Search App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/webble.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### 3. Build APK Automatically

Once pushed, GitHub Actions will automatically:
1. Set up Flutter
2. Install dependencies
3. Build your APK
4. Make it available for download

### 4. Download Your APK

1. Go to your repo: `https://github.com/YOUR_USERNAME/webble`
2. Click **Actions** tab
3. Click on the latest workflow run
4. Scroll down to **Artifacts**
5. Download `webble-debug-apk` or `webble-release-apk`

### 5. Install on Your Phone

1. Transfer the APK to your Android phone
2. Enable "Install from Unknown Sources" in Settings
3. Open the APK file and install

## Build with Custom Backend URL

Once you deploy your backend, you can build with the production URL:

1. Go to **Actions** tab
2. Click **Build Android APK** workflow
3. Click **Run workflow**
4. Enter your backend URL: `https://your-backend.deta.app`
5. Click **Run workflow**
6. Wait ~5 minutes
7. Download the APK from Artifacts

## Build AAB for Play Store

When ready to publish:

1. Go to **Actions** tab
2. Click **Build Android App Bundle (AAB) for Play Store**
3. Click **Run workflow**
4. Enter:
   - Backend URL: `https://your-backend.deta.app`
   - Version: `1.0.0`
5. Click **Run workflow**
6. Download the AAB file
7. Upload to Google Play Console

## What Gets Built

### Debug APK
- Larger file size (~50MB)
- Includes debugging info
- Good for testing
- Available after every push

### Release APK
- Smaller file size (~20MB)
- Optimized and minified
- Ready for distribution
- Needs signing for Play Store

### Release AAB (App Bundle)
- Required for Play Store
- Google optimizes for each device
- Smallest download size for users

## Troubleshooting

### Build Failed?

Check the logs in Actions tab. Common issues:

1. **Syntax error in code** - Fix and push again
2. **Missing dependencies** - Already configured, shouldn't happen
3. **Timeout** - Re-run the workflow

### Can't Download Artifacts?

- Artifacts expire after 30-90 days
- Re-run the workflow to generate new ones

### Want to Build Locally Later?

You can always install Flutter later:
```bash
# Quick install
winget install --id=Google.Flutter -e
```

## Cost

**$0** - Completely free for public repositories!

GitHub gives you:
- 2,000 minutes/month of Actions (free tier)
- Each build takes ~5 minutes
- = ~400 builds per month for free

## Next Steps

1. **Push your code to GitHub** (see Step 2 above)
2. **Wait 5 minutes** for automatic build
3. **Download APK** from Actions tab
4. **Test on your phone**
5. **Deploy backend** to Deta Space
6. **Build with production URL**
7. **Publish to Play Store**

## Pro Tips

### Automatic Builds on Every Push
Every time you push code, a new APK is built automatically. Great for:
- Testing new features
- Sharing with beta testers
- Continuous deployment

### Manual Builds with Custom Settings
Use "Run workflow" button to:
- Build with different backend URLs
- Test staging vs production
- Create special builds

### Keep Your Repo Private
If you want privacy:
1. Make repo private (free on GitHub)
2. You still get 2,000 free minutes/month
3. Only you can download the APKs

## Example Timeline

```
0:00 - Push code to GitHub
0:30 - GitHub Actions starts
1:00 - Flutter installed
2:00 - Dependencies downloaded
4:00 - APK built
5:00 - APK available for download ✅
```

Total: **5 minutes** from push to APK!

## Summary

You don't need Flutter installed locally. Just:
1. Push to GitHub
2. Wait 5 minutes
3. Download APK
4. Install on phone

It's that simple! 🚀
