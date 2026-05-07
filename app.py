import requests
import streamlit as st
from config import OLLAMA_URL, OLLAMA_MODEL
from tools.rag_tool import search_building_docs
from tools.calculator_tool import calculate_area
from tools.classifier_tool import classify_structure
from tools.checklist_tool import generate_checklist

st.set_page_config(
    page_title="Ontario Permit Agent",
    page_icon="🏗️"
)

st.title("🏗️ Ontario Permit Agent")
st.write("Ask questions about Ontario permit/building documents.")

question = st.text_input("Ask a permit or building-code question:")
st.subheader("Project Details")

length = st.number_input("Length (ft)", min_value=0.0, value=10.0)
width = st.number_input("Width (ft)", min_value=0.0, value=16.0)
description = st.text_input("Structure description", value="10x16 shed")

def generate_answer(question: str, context: str, project_area: dict, structure_type: str, checklist: list[str]) -> str:
    prompt = f"""
You are Ontario Permit Agent and never anything else.

Use ONLY the provided document context to answer the user's question.

Rules:
- If the answer is not found in the context, say you could not find it.
- Do not guess.
- Include source document and page number when available.
- Keep the answer practical and clear.
- This is informational only, not legal advice.
- If the question is outside the scope of Ontario permits/building codes, say you cannot answer it.

Project details:
- Structure type: {structure_type}
- Area: {project_area["area_sq_ft"]} sq ft
- Area: {project_area["area_sq_m"]} sq m
- Checklist items: {checklist}

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


if st.button("Ask") and question:
    with st.spinner("Searching documents..."):
        context = search_building_docs(question)
        project_area = calculate_area(length, width)
        structure_type = classify_structure(description)
        checklist = generate_checklist(
            structure_type,
            project_area["area_sq_ft"]
        )

        answer = generate_answer(
             question,
             context,
             project_area,
             structure_type,
             checklist
    )

    st.subheader("Answer")
    st.write(answer)
    st.subheader("Project Analysis")
    st.write(f"Structure type: {structure_type}")
    st.write(f"Area: {project_area['area_sq_ft']} sq ft / {project_area['area_sq_m']} sq m")

    st.subheader("Permit Checklist")
    for item in checklist:
        st.write(f"- {item}")

    with st.expander("Retrieved document context"):
        st.write(context)