import asyncio
from typing import Optional

import bcrypt
from database.repositories.message_repository import MessageRepository
from database.repositories.session_repository import SessionRepository
from database.repositories.user_repository import UserRepository
from fastapi import Body, FastAPI, HTTPException
from vora import Vora

app = FastAPI(title="Vora AI Backend", version="0.1.0")
vora = Vora()


@app.post("/send_message")
async def chat(
    user_id: int = Body(...),
    session_id: Optional[int] = Body(None),
    question: str = Body(...),
) -> dict:
    session_repo = SessionRepository()
    message_repo = MessageRepository()

    try:
        if not session_id or not session_repo.get_by_id(session_id):
            session_id = session_repo.insert(user_id)

        message_repo.insert("user", question, session_id)

        try:
            answer: str = await vora.answer(question)
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
    if not user or not bcrypt.checkpw(password.encode(), user[2].encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials.")

    return {"message": "Login successful.", "user_name": user_name}


if __name__ == "__main__":

    async def test_chat(session_id: int, user_id: int, question: str):
        session_repo = SessionRepository()
        message_repo = MessageRepository()
        question = "como fritar um ovo?"

        try:
            if not session_id or not session_repo.get_by_id(session_id):
                session_id = session_repo.insert(user_id)

            message_repo.insert("user", question, session_id)

            try:
                answer: str = await vora.answer(question)
            except Exception as exc:
                raise HTTPException(
                    status_code=500, detail=f"Failed to generate answer: {exc}"
                ) from exc

            message_repo.insert("assistent", answer, session_id)

        finally:
            session_repo.close()
            message_repo.close()

        return {"answer": answer, "session_id": session_id}

    asyncio.run(test_chat(1, 6, "como fritar um ovo?"))
