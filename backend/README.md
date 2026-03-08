# Backend

Vora AI API (FastAPI, LangChain, OpenAI, MySQL).

**Setup:** `pip install -r requirements.txt`, create DB `vora_ai`, copy `.env.example` to `.env` and set `OPENAI_API_KEY` and MySQL settings.

**Run:** `python run.py` (or `uvicorn main:app --reload` from backend folder).

**Test:** `python tests/test_chat_api.py` with server running.

Endpoints: `POST /chat`, `GET /chat/history/{session_id}`, `GET /health`.
