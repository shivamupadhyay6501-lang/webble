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

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """Main endpoint: search web and generate AI answer"""
    
    if not request.question or len(request.question.strip()) < 3:
        raise HTTPException(status_code=400, detail="Question too short")
    
    # Step 1: Search DuckDuckGo
    ddg_results = await search_duckduckgo(request.question)
    
    # Step 2: Extract relevant information
    context, sources = extract_search_results(ddg_results)
    
    if not context or context == "No detailed results found.":
        return AnswerResponse(
            answer="I couldn't find relevant information for your question. Try rephrasing it.",
            sources=[],
            raw_search_data=ddg_results
        )
    
    # Step 3: Generate AI answer
    ai_answer = await ask_ai_model(request.question, context)
    
    return AnswerResponse(
        answer=ai_answer,
        sources=sources[:5],  # Limit to top 5 sources
        raw_search_data=ddg_results
    )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
