from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from vora import Vora


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


app = FastAPI(title="Vora AI Backend", version="0.1.0")
vora = Vora()


@app.post("/chat", response_model=AnswerResponse)
async def chat(request: QuestionRequest) -> AnswerResponse:
    try:
        answer: str = await vora.answer(request.question)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to generate answer: {exc}") from exc

    return AnswerResponse(answer=answer)

