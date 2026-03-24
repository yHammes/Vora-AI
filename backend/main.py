from fastapi import FastAPI, HTTPException, Body
from vora import Vora


app = FastAPI(title="Vora AI Backend", version="0.1.0")
vora = Vora()
users_db: dict[str, str] = {}


@app.post("/chat")
async def chat(question: str = Body(..., embed=True)) -> dict:
    try:
        answer: str = await vora.answer(question)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to generate answer: {exc}") from exc

    return {"answer": answer}


@app.post("/users")
async def create_user(
    user_name: str = Body(...),
    password: str = Body(...),
) -> dict:
    if user_name in users_db:
        raise HTTPException(status_code=409, detail="User already exists.")

    users_db[user_name] = password

    return {"message": "User created successfully.", "user_name": user_name}
