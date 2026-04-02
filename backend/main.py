from fastapi import Body, FastAPI, HTTPException
from vora import Vora
from database.repositories.user_repository import UserRepository
import bcrypt

app = FastAPI(title="Vora AI Backend", version="0.1.0")
vora = Vora()


@app.post("/send_message")
async def chat(question: str = Body(..., embed=True)) -> dict:
    try:
        answer: str = await vora.answer(question)
    except Exception as exc:
        raise HTTPException(
            status_code=500, detail=f"Failed to generate answer: {exc}"
        ) from exc

    return {"answer": answer}


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
