import os
from typing import Optional

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


class Vora:
    def __init__(self) -> None:
        load_dotenv()
        self._chain = self._build_chain()

    @staticmethod
    def _build_chain():
        api_key: Optional[str] = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError("GOOGLE_API_KEY is not set in .env or environment.")

        prompt = ChatPromptTemplate.from_template(
            "You are a helpful assistant. Answer the user's question clearly.\n\nQuestion: {question}"
        )

        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

        parser = StrOutputParser()

        return prompt | llm | parser

    async def answer(self, question: str) -> str:
        return await self._chain.ainvoke({"question": question})
