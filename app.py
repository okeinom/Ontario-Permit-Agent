import requests
import streamlit as st
from config import OLLAMA_URL, OLLAMA_MODEL
from tools.rag_tool import search_building_docs

st.set_page_config(
    page_title="Ontario Permit Agent",
    page_icon="🏗️"
)

st.title("🏗️ Ontario Permit Agent - Phase 1")
st.write("Ask questions about Ontario permit/building documents.")

question = st.text_input("Ask a permit or building-code question:")


def generate_answer(question: str, context: str) -> str:
    prompt = f"""
You are Ontario Permit Agent.

Use ONLY the provided document context to answer the user's question.

Rules:
- If the answer is not found in the context, say you could not find it.
- Do not guess.
- Include source document and page number when available.
- Keep the answer practical and clear.
- This is informational only, not legal advice.

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
        answer = generate_answer(question, context)

    st.subheader("Answer")
    st.write(answer)

    with st.expander("Retrieved document context"):
        st.write(context)