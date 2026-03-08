import os
from dotenv import load_dotenv
import uvicorn

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
