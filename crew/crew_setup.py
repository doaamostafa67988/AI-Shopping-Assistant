import re
import sys
import time
from pathlib import Path

from crewai import Crew
from crew.agents import create_agents
from crew.tasks import create_tasks

# --- Workaround for crewAI issue #5886 ---------------------------------
# crewAI's prompt-caching feature tags messages with a "cache_breakpoint"
# key, but only strips it back out for the Anthropic provider adapter.
# For Groq (and other OpenAI-compatible providers) the raw flag gets sent
# straight through, and Groq's API rejects it with:
#   "property 'cache_breakpoint' is unsupported"
# mark_cache_breakpoint() is imported locally at call time inside crewai's
# executor, so patching it here (anytime before kickoff) is enough - no
# need to reach into crewai's internals beyond this.
# Upstream tracking: https://github.com/crewAIInc/crewAI/issues/5886
import crewai.llms.cache as _crewai_cache
_crewai_cache.mark_cache_breakpoint = lambda msg: msg
# -------------------------------------------------------------------------

MAX_ATTEMPTS = 3
DEFAULT_BACKOFF_SECONDS = 15

_RETRY_AFTER_RE = re.compile(r"try again in\s+([\d.]+)\s*s", re.IGNORECASE)


def _seconds_to_wait(exc: Exception) -> float:
    """Groq's rate-limit errors say exactly how long to wait - use that
    instead of guessing with a short fixed backoff, which was too short
    (2-6s) against Groq's actual reset windows (up to ~30s)."""
    match = _RETRY_AFTER_RE.search(str(exc))
    if match:
        return float(match.group(1)) + 1  # small buffer
    return DEFAULT_BACKOFF_SECONDS


def run_crew(product, websites):
    researcher, analyst = create_agents()
    t1, t2 = create_tasks(product, websites, researcher, analyst)

    crew = Crew(
        agents=[researcher, analyst],
        tasks=[t1, t2],
        verbose=True
    )

    last_error = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            return crew.kickoff()
        except Exception as exc:
            last_error = exc
            print(f"[run_crew] attempt {attempt}/{MAX_ATTEMPTS} failed: {exc}")
            if attempt < MAX_ATTEMPTS:
                wait = _seconds_to_wait(exc)
                print(f"[run_crew] waiting {wait:.1f}s before retrying")
                time.sleep(wait)

    # All attempts failed - surface the last error to app.py's try/except
    raise last_error
