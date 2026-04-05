import asyncio
from typing import Optional

import bcrypt
from database.repositories.message_repository import MessageRepository
from database.repositories.session_repository import SessionRepository
from database.repositories.user_repository import UserRepository
from fastapi import Body, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from vora import Vora

app = FastAPI(title="Vora AI Backend", version="0.1.0")
vora = Vora()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://vora-ai-ruddy.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/send_message")
async def chat(
    user_id: int = Body(...),
    session_id: Optional[int] = Body(None),
    question: str = Body(...),
) -> dict:
    session_repo = SessionRepository()
    message_repo = MessageRepository()

    try:
        if not session_repo.get_by_id(session_id):
            session_id = session_repo.insert(user_id)

        history = message_repo.get_messages_by_session_id(session_id)
        message_repo.insert("user", question, session_id)

        try:
            answer: str = await vora.answer(question, history)
        except Exception as exc:
            raise HTTPException(
                status_code=500, detail=f"Failed to generate answer: {exc}"
            ) from exc

        message_repo.insert("assistent", answer, session_id)

    finally:
        session_repo.close()
        message_repo.close()

    return {"answer": answer, "session_id": session_id}


@app.post("/register")
async def register(user_name: str = Body(...), password: str = Body(...)):
    repo = UserRepository()
    try:
        if repo.get_by_name(user_name):
            raise HTTPException(status_code=409, detail="O Usuario já existe!.")

        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        repo.insert(user_name, hashed)
    finally:
        repo.close()
    return {"message": "User created successfully.", "user_name": user_name}


@app.post("/login")
async def login(user_name: str = Body(...), password: str = Body(...)):
    repo = UserRepository()
    try:
        user = repo.get_by_name(user_name)
    finally:
        repo.close()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials.")

    user_password = user[2]
    user_id = user[0]

    if not bcrypt.checkpw(password.encode(), user_password.encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials.")

    return {"message": "Login successful.", "user_id": user_id, "user_name": user_name}
