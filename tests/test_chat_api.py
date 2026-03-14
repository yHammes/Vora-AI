"""Run with: python tests/test_chat_api.py (from backend folder). Start server first: python run.py"""
import httpx

BASE = "http://127.0.0.1:8000"

def main():
    print("1. Health")
    r = httpx.get(f"{BASE}/health", timeout=5.0)
    print(r.json())
    print("2. Send message")
    r = httpx.post(f"{BASE}/chat", json={"message": "What are good sources of protein?", "session_id": 1}, timeout=30.0)
    print(r.json().get("response", "")[:150], "...")
    print("3. History")
    r = httpx.get(f"{BASE}/chat/history/1", timeout=10.0)
    print(len(r.json()), "messages")

if __name__ == "__main__":
    main()
