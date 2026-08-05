from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

def get_search_tool():
    load_dotenv()
    if not os.getenv("SERPER_API_KEY"):
        raise ValueError("SERPER_API_KEY is missing. Add it to your .env file.")
 
    # Fewer results per search = far fewer tokens sent back to the LLM on
    # every tool call, which matters a lot on Groq's free-tier per-minute
    # token limits.
    return SerperDevTool(n_results=5)
