import os
import sys
from pathlib import Path

vendor_litellm = Path(__file__).resolve().parent.parent / ".vendor_litellm"
if vendor_litellm.exists():
    sys.path.insert(0, str(vendor_litellm))

from crewai import LLM 
from dotenv import load_dotenv

load_dotenv()
def getllm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Add it to your .env file.")

    llm = LLM(
        model=os.getenv("LLM_MODEL_NAME", "groq/qwen/qwen3.6-27b"),
        api_key=api_key,
        temperature=0.4,
        # Groq reasoning models accept a reasoning_effort knob, but the
        # allowed values differ by model family: gpt-oss takes
        # low/medium/high, Qwen3 models take none/default. "none" disables
        # reasoning for Qwen, keeping answers direct and tool-call-friendly.
        # If you switch LLM_MODEL_NAME back to an openai/gpt-oss-* model,
        # also set LLM_REASONING_EFFORT=low in .env.
        reasoning_effort=os.getenv("LLM_REASONING_EFFORT", "none"),
    )
    return llm
