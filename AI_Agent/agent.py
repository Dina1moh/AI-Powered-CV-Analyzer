# AI_Agent/agent.py

import sys
from pathlib import Path
import os
from typing import Dict, List, Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent

from .all_tools import base_tools


# Load Environment

load_dotenv()

OPENAI_API_KEY_AGENT = os.getenv("OPENAI_API_KEY_AGENT")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")


# =========================
# LLM Configuration
# =========================
llm = ChatOpenAI(
    model=OPENAI_MODEL_NAME,
    temperature=0,
    openai_api_key=OPENAI_API_KEY_AGENT,
    openai_api_base=OPENAI_API_BASE,
)


# =========================
# Memory (optional but useful)
# =========================


# =========================
# Base System Prompt
# =========================
BASE_SYSTEM_PROMPT = """
You are a professional AI assistant specialized in:

1) CV Analysis Interpretation
2) Career Guidance
3) Skill Gap Recommendations
4) Document Question Answering (RAG)

Follow all rules strictly.

--------------------------------------------------

CORE RULES

- Always respond with structured Markdown.
- Never fabricate information.
- If information is missing, clearly say so.
- Be precise and helpful.

--------------------------------------------------

CV ANALYSIS CONTEXT

The user CV analysis data may be provided.

It includes:

- match_percentage
- strengths
- gaps
- recommended_skills
- improvement_suggestions

When answering CV-related questions:

1. Use ONLY the provided CV data.
2. Extract missing skills from gaps.
3. Prioritize recommended_skills.
4. Base advice on improvement_suggestions.
5. Do NOT invent new skills.

If CV data is missing say:

"The CV analysis data was not provided."

--------------------------------------------------

TOOL STRATEGY (STRICT ORDER)

DOCUMENT QUESTIONS:

If a document tool exists:

1. ALWAYS use document_search first.
2. If found → answer from document.
3. If not found → say:

"The requested information was not found in the provided document."

Then external search is allowed.

EXTERNAL SEARCH:

Only after document check.

State:

"Based on external search results..."

--------------------------------------------------

TRANSPARENCY

Always mention source:

• Based on CV analysis...
• According to the provided document...
• Based on external search...
"""


# =========================
# Create Agent Function
# =========================
def create_agent(
    tools: Optional[List] = None,
    cv_analysis: Optional[Dict] = None,
):
    """
    Create AI agent with optional CV analysis context.
    """

    tools = tools or base_tools

    if cv_analysis:
        cv_context = f"""


match_percentage: {cv_analysis.get("match_percentage")}

strengths:
{cv_analysis.get("strengths")}

gaps:
{cv_analysis.get("gaps")}

recommended_skills:
{cv_analysis.get("recommended_skills")}

improvement_suggestions:
{cv_analysis.get("improvement_suggestions")}


IMPORTANT:
This is the ONLY source of truth for CV answers.
Do NOT invent information.
"""
    else:
        cv_context = "\nNo CV analysis data was provided.\n"

    final_prompt = BASE_SYSTEM_PROMPT + "\n" + cv_context

   
    agent = create_deep_agent(
        llm,
        tools=tools,
        system_prompt=final_prompt,
        debug=True,
    )

    return agent


def ask_agent(
    message: str,
    cv_analysis: Optional[Dict] = None,
    tools: Optional[List] = None,
) -> str:
    """
    Simple helper to send message to agent.
    """

    agent = create_agent(
        tools=tools,
        cv_analysis=cv_analysis,
    )

    response = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": message}
            ]
        }
    )

    messages = response.get("messages", [])

    for msg in reversed(messages):
        if hasattr(msg, "content") and msg.content:
            return msg.content

    return "No response generated."



base_agent = create_agent()