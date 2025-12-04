# What You Need to Provide - Webble Play Store Release

## 1. App Identity (REQUIRED)

### Package Name
Choose a unique package name (reverse domain format):
- Example: `com.yourname.webble`
- Example: `com.johndoe.webble`
- Example: `io.github.username.webble`

**Where to change it:**
- `frontend/android/app/build.gradle` (line 35 and 40)
- `frontend/android/app/src/main/AndroidManifest.xml` (package attribute)
- `frontend/android/app/src/main/kotlin/com/webble/app/MainActivity.kt` (package line)

### Your Information
- **Developer/Company Name**: _________________
- **Support Email**: _________________
- **Website** (optional): _________________

## 2. Backend Deployment (REQUIRED)

You need to deploy the backend and give me the URL.

### Option A: Deta Space (Easiest, 100% Free)
```bash
# Install CLI
iwr https://get.deta.dev/space-cli.ps1 -useb | iex

# Deploy
cd backend
space login
space new
space push
```

**Your Deta URL**: ________________________________
(Will look like: `https://webble-1-x1234567.deta.app`)

### Option B: Railway.app (Free tier)
1. Sign up at railway.app
2. Deploy from GitHub
3. Set root directory to `backend`

**Your Railway URL**: ________________________________

### Option C: Render.com (Free tier)
Similar to Railway

**Your Render URL**: ________________________________

## 3. HuggingFace Token (REQUIRED)

Get free token at: https://huggingface.co/settings/tokens

**Your Token**: hf_________________________________

Set it in your backend:
```bash
space env add HUGGINGFACE_API_KEY hf_your_token
```

## 4. Privacy Policy (REQUIRED by Play Store)

You MUST host a privacy policy online. Options:

### Option A: GitHub Pages (Free)
I can create the file, you just need to:
1. Create a GitHub repo
2. Enable GitHub Pages in settings
3. Give me the URL

**Your Privacy Policy URL**: ________________________________

### Option B: Your Website
If you have a website, I'll create the HTML file.

**Your Website URL**: ________________________________

### Option C: Google Sites (Free)
Create a free site at sites.google.com

## 5. App Assets

### App Icon (REQUIRED)
- Size: 512x512 pixels
- Format: PNG with transparency
- No text or complex details (will be scaled down)

**Do you have an icon?** [ ] Yes [ ] No (I'll create a placeholder)

### Feature Graphic (REQUIRED for Play Store)
- Size: 1024x500 pixels
- Format: PNG or JPG
- Used in Play Store listing

**Do you have a feature graphic?** [ ] Yes [ ] No (I'll create one)

### Screenshots (REQUIRED, at least 2)
- Phone screenshots showing the app
- Size: 1080x1920 or similar

**Do you have screenshots?** [ ] Yes [ ] No (I'll help generate)

## 6. Play Store Listing Text

### App Name (max 30 chars)
Default: "Webble"
**Your choice**: ________________________________

### Short Description (max 80 chars)
Default: "Free AI-powered web search assistant"
**Your choice**: ________________________________

### Full Description (max 4000 chars)
I'll create this, but any specific features you want highlighted?
________________________________
________________________________

### Category
Default: Tools
**Your choice**: [ ] Tools [ ] Productivity [ ] Education [ ] Other: ________

## 7. Google Play Developer Account

**Do you have one?** [ ] Yes [ ] No

If No: You need to create one at https://play.google.com/console
- Cost: $25 one-time fee
- Requires Google account
- Takes ~48 hours to approve

## Quick Checklist

Fill this out and I'll configure everything:

```
PACKAGE_NAME=com.yourname.webble
DEVELOPER_NAME=Your Name
SUPPORT_EMAIL=your@email.com
BACKEND_URL=https://your-backend.deta.app
HUGGINGFACE_TOKEN=hf_your_token
PRIVACY_POLICY_URL=https://yoursite.com/privacy
APP_NAME=Webble
```

## What Happens Next

Once you provide the above:

1. I'll update all configuration files
2. Generate signing key instructions
3. Create privacy policy (if needed)
4. Build release AAB file
5. Provide step-by-step Play Store upload guide

## Minimum to Get Started

If you want to start NOW with minimal setup:

1. **Backend URL** - Deploy to Deta Space (5 minutes)
2. **HuggingFace Token** - Sign up and copy token (2 minutes)
3. **Package Name** - Just pick one (e.g., `com.yourname.webble`)

I can use placeholders for everything else and you can update later!
