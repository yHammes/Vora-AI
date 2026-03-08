import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database import init_db, get_history
from ai import chat

app = FastAPI(title="Vora AI")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class ChatRequest(BaseModel):
    message: str
    session_id: int = 1


class ChatResponse(BaseModel):
    response: str
    session_id: int


@app.on_event("startup")
def startup():
    init_db()  # TODO: inicializar banco quando a conexão for implementada


@app.post("/chat", response_model=ChatResponse)
def post_chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(400, "Message cannot be empty")
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(500, "OPENAI_API_KEY not set in .env")
    try:
        response = chat(req.session_id, req.message.strip())
        return ChatResponse(response=response, session_id=req.session_id)
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/chat/history/{session_id}")
def get_chat_history(session_id: int):
    try:
        rows = get_history(session_id)
        return [{"role": "bot" if r["role"] == "assistant" else r["role"], "content": r["content"]} for r in rows]
    except Exception as e:
        raise HTTPException(500, str(e))


@app.get("/health")
def health():
    return {"status": "ok"}
