from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = FastAPI(title="Webble API")

# Enable CORS for Flutter app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")
HUGGINGFACE_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    sources: list[dict]
    raw_search_data: dict

async def search_duckduckgo(query: str) -> dict:
    """Search DuckDuckGo free API"""
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"DuckDuckGo search failed: {str(e)}")

def extract_search_results(ddg_data: dict) -> tuple[str, list[dict]]:
    """Extract useful information from DuckDuckGo response"""
    sources = []
    context_parts = []
    
    # Extract abstract
    if ddg_data.get("AbstractText"):
        context_parts.append(f"Overview: {ddg_data['AbstractText']}")
        if ddg_data.get("AbstractURL"):
            sources.append({
                "title": ddg_data.get("Heading", "Overview"),
                "url": ddg_data["AbstractURL"],
                "snippet": ddg_data["AbstractText"][:200]
            })
    
    # Extract related topics
    for topic in ddg_data.get("RelatedTopics", [])[:5]:
        if isinstance(topic, dict) and topic.get("Text"):
            context_parts.append(topic["Text"])
            if topic.get("FirstURL"):
                sources.append({
                    "title": topic.get("Text", "")[:100],
                    "url": topic["FirstURL"],
                    "snippet": topic["Text"][:200]
                })
    
    context = "\n".join(context_parts) if context_parts else "No detailed results found."
    return context, sources

async def ask_ai_model(question: str, context: str) -> str:
    """Use HuggingFace free inference API"""
    
    if not HUGGINGFACE_API_KEY:
        # Fallback: simple summarization without AI
        return f"Based on web search:\n\n{context[:500]}..."
    
    url = f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    prompt = f"""Based on the following web search results, provide a clear and concise answer to the question.

Question: {question}

Search Results:
{context[:2000]}

Answer:"""
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7,
            "top_p": 0.9,
            "return_full_text": False
        }
    }
    
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            
            if response.status_code == 503:
                # Model is loading, return context-based answer
                return f"Based on web search results:\n\n{context[:500]}"
            
            response.raise_for_status()
            result = response.json()
            
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", context[:500])
            return context[:500]
            
        except Exception as e:
            # Fallback to context if AI fails
            return f"Based on web search:\n\n{context[:500]}"

@app.get("/")
async def root():
    return {"message": "Webble API - Free AI Web Search Assistant"}

def is_casual_question(question: str) -> bool:
    """Check if question is casual chat (no web search needed)"""
    casual_patterns = [
        'hi', 'hello', 'hey', 'hii', 'hiii',
        'how are you', 'whats up', "what's up",
        'good morning', 'good evening', 'good night',
        'thanks', 'thank you', 'bye', 'goodbye',
        'i am sad', "i'm sad", 'i am happy', "i'm happy",
        'i am tired', "i'm tired", 'i am bored', "i'm bored",
        'tell me a joke', 'make me laugh',
        'who are you', 'what are you', 'your name',
    ]
    
    question_lower = question.lower().strip()
    
    # Check if it's a casual greeting or emotion
    for pattern in casual_patterns:
        if pattern in question_lower:
            return True
    
    # Check if it's very short (likely casual)
    if len(question_lower.split()) <= 3 and '?' not in question_lower:
        return True
    
    return False

async def chat_directly(question: str) -> str:
    """Direct chat without web search for casual questions"""
    
    question_lower = question.lower().strip()
    
    # Detailed fallback responses
    if any(word in question_lower for word in ['hi', 'hello', 'hey', 'hii']):
        return "Hello! 👋 I'm Webble, your AI assistant. I can search the web for information or just chat with you. What would you like to talk about?"
    
    if 'how are you' in question_lower:
        return "I'm doing great, thanks for asking! 😊 I'm here and ready to help you with anything. How are you doing?"
    
    if any(word in question_lower for word in ['sad', 'depressed', 'down', 'unhappy']):
        return "I'm sorry you're feeling this way. 💙 Remember, it's completely normal to feel sad sometimes. Talking about it can help. Would you like to share what's on your mind, or shall I help you with something to take your mind off things?"
    
    if any(word in question_lower for word in ['happy', 'great', 'awesome', 'excited']):
        return "That's wonderful! 🎉 I'm so glad you're feeling happy! Your positive energy is contagious. What's making you feel so good today?"
    
    if any(word in question_lower for word in ['tired', 'exhausted', 'sleepy']):
        return "I understand, we all get tired sometimes. 😴 Make sure to get some rest when you can. In the meantime, how can I help make things easier for you?"
    
    if any(word in question_lower for word in ['bored', 'boring']):
        return "Feeling bored? Let's fix that! 🎯 I can help you learn something new, find interesting facts, or we can just chat. What sounds good to you?"
    
    if 'joke' in question_lower or 'funny' in question_lower:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
            "What do you call a bear with no teeth? A gummy bear! 🐻",
            "Why don't eggs tell jokes? They'd crack each other up! 🥚",
        ]
        import random
        return random.choice(jokes)
    
    if any(word in question_lower for word in ['who are you', 'what are you', 'your name']):
        return "I'm Webble! 🤖 I'm an AI assistant that can search the web to answer your questions or just have a friendly chat with you. I'm here to help make your day easier and more interesting!"
    
    if any(word in question_lower for word in ['thank', 'thanks']):
        return "You're very welcome! 😊 I'm always happy to help. Is there anything else you'd like to know?"
    
    if any(word in question_lower for word in ['bye', 'goodbye', 'see you']):
        return "Goodbye! 👋 It was nice chatting with you. Come back anytime you need help or just want to talk!"
    
    if 'good morning' in question_lower:
        return "Good morning! ☀️ Hope you have a wonderful day ahead! How can I help you today?"
    
    if 'good night' in question_lower:
        return "Good night! 🌙 Sleep well and sweet dreams! See you tomorrow!"
    
    # Default friendly response
    return "I'm here to help! 😊 You can ask me anything - I'll search the web for factual questions or just chat with you about how you're feeling. What's on your mind?"
    
    # Use HuggingFace for better casual chat
    url = f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    prompt = f"""You are Webble, a friendly AI assistant. Have a natural, warm conversation.

User: {question}
Assistant:"""
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.9,
            "top_p": 0.95,
            "return_full_text": False
        }
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            
            if response.status_code == 503:
                return "I'm here to chat! What's on your mind?"
            
            response.raise_for_status()
            result = response.json()
            
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", "I'm here to help! What would you like to talk about?")
            return "I'm here to help! What would you like to talk about?"
            
        except Exception:
            return "I'm here to chat! How can I help you?"

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """Main endpoint: smart routing between casual chat and web search"""
    
    if not request.question or len(request.question.strip()) < 2:
        raise HTTPException(status_code=400, detail="Question too short")
    
    # Check if it's a casual question
    if is_casual_question(request.question):
        # Direct chat without web search
        ai_answer = await chat_directly(request.question)
        return AnswerResponse(
            answer=ai_answer,
            sources=[],
            raw_search_data={}
        )
    
    # For factual questions, search the web
    # Step 1: Search DuckDuckGo
    ddg_results = await search_duckduckgo(request.question)
    
    # Step 2: Extract relevant information
    context, sources = extract_search_results(ddg_results)
    
    if not context or context == "No detailed results found.":
        # If no web results, try direct AI chat
        ai_answer = await chat_directly(request.question)
        return AnswerResponse(
            answer=ai_answer,
            sources=[],
            raw_search_data=ddg_results
        )
    
    # Step 3: Generate AI answer with web context
    ai_answer = await ask_ai_model(request.question, context)
    
    return AnswerResponse(
        answer=ai_answer,
        sources=sources[:5],
        raw_search_data=ddg_results
    )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
