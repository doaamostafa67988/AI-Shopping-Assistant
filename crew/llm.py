from crewai import LLM 
import os
from dotenv import load_dotenv

load_dotenv()
def getllm():
    llm = LLM(
        model="groq/meta-llama/llama-4-scout-17b-16e-instruct",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.4,
    )
    return llm