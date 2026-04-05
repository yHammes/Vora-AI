import asyncio

from vora import Vora


async def main() -> None:
    vora = Vora()

    question = input("Enter your question: ")
    answer = await vora.answer(question, [])

    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())
