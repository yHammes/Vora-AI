import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from database import get_history, save_message

PROMPT = """You are a helpful assistant for food, nutrition, and cooking.
Answer clearly about ingredients, diets, recipes, and healthy eating."""


def chat(session_id: int, message: str) -> str:
    save_message(session_id, "user", message)
    history = get_history(session_id)
    messages = [SystemMessage(content=PROMPT)]
    for h in history:
        if h["role"] == "user":
            messages.append(HumanMessage(content=h["content"]))
        else:
            messages.append(AIMessage(content=h["content"]))
    messages.append(HumanMessage(content=message))
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)
    reply = llm.invoke(messages)
    answer = reply.content if hasattr(reply, "content") else str(reply)
    save_message(session_id, "assistant", answer)
    return answer
