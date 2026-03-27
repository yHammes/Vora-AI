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

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", open("prompts/support_agent.md").read()),
                ("user", "Mensagem do usuario: {question}"),
            ]
        )

        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

        parser = StrOutputParser()

        return prompt | llm | parser

    async def answer(self, question: str) -> str:
        return await self._chain.ainvoke({"question": question})
