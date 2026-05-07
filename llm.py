import requests
from config import OLLAMA_URL, OLLAMA_MODEL


def generate_answer(
    question: str,
    context: str,
    project_area: dict | None = None,
    structure_type: str | None = None,
    checklist: list[str] | None = None
) -> str:
     area_sq_ft = project_area["area_sq_ft"] if project_area else "Not calculated"
     area_sq_m = project_area["area_sq_m"] if project_area else "Not calculated"
     structure = structure_type or "Not classified"
     checklist_items = checklist or []

     prompt = f"""
You are Ontario Permit Agent.

Use ONLY the provided document context and project details.

Rules:
- Do not guess.
- If the answer is not found in the context, say you could not find it.
- Include source document and page number when available.
- Be practical and clear.
- This is informational only, not legal advice.

Project details:
- Structure type: {structure}
- Area: {area_sq_ft} sq ft
- Area: {area_sq_m} sq m
- Checklist items: {checklist_items}

Context:
{context}

Question:
{question}

Answer:
"""

     response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

     response.raise_for_status()
     return response.json()["response"]

def generate_tool_plan(question: str) -> list[str]:
    prompt = f"""
You are an AI agent planner.

Decide which tools are needed to answer the question.

Available tools:
- classify_structure
- calculate_area
- search_building_docs
- generate_checklist

Rules:
- Only include tools that are necessary
- Always include search_building_docs if question is about rules, permits, or building code
- Output ONLY a comma-separated list of tool names

Question:
{question}

Tools:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    text = response.json()["response"]

    return [t.strip() for t in text.split(",") if t.strip()]