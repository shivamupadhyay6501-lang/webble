# Webble - Free AI Web-Search Assistant

Every question is automatically searched on the web and answered using free AI models.

## Architecture
- **Backend**: Python FastAPI
- **Frontend**: Flutter
- **Search**: DuckDuckGo Free API (no key required)
- **AI**: HuggingFace Free Inference API
- **Hosting**: Deta Space (100% free)

## Quick Start

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend Setup
```bash
cd frontend
flutter pub get
flutter run
```

## Deployment to Deta Space

1. Install Deta Space CLI:
```bash
curl -fsSL https://get.deta.dev/space-cli.sh | sh
```

2. Login to Deta Space:
```bash
space login
```

3. Deploy:
```bash
cd backend
space push
```

## Environment Variables

Create `backend/.env`:
```
HUGGINGFACE_API_KEY=your_free_key_here
```

Get free HuggingFace API key at: https://huggingface.co/settings/tokens

## How It Works

1. User asks a question in Flutter app
2. Backend searches DuckDuckGo API (free, no key)
3. Backend sends results to HuggingFace free model
4. AI summarizes the answer
5. Frontend displays answer + citations
