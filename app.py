import streamlit as st
from agent import run_permit_agent

st.set_page_config(
    page_title="Ontario Permit Agent",
    page_icon="🏗️"
)

st.title("🏗️ Ontario Permit Agent")
st.write("Agentic RAG assistant for Ontario permit/building questions.")

question = st.text_input("Ask a permit or building-code question:")

st.subheader("Project Details")

length = st.number_input("Length (ft)", min_value=0.0, value=10.0)
width = st.number_input("Width (ft)", min_value=0.0, value=16.0)
description = st.text_input("Structure description", value="10x16 shed")


if st.button("Ask Agent") and question:
    with st.spinner("Agent is working..."):
        result = run_permit_agent(
            question=question,
            length=length,
            width=width,
            description=description
        )

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Agent Steps")
    for step in result["steps"]:
        st.write(f"- {step}")

    st.subheader("Project Analysis")
    st.write(f"Structure type: {result['structure_type'] or 'Not classified'}")
    if result["project_area"]:
     st.write(
        f"Area: {result['project_area']['area_sq_ft']} sq ft / "
        f"{result['project_area']['area_sq_m']} sq m"
      )
    else:
     st.write("Area: Not calculated")

    st.subheader("Permit Checklist")
    for item in result["checklist"]:
        st.write(f"- {item}")

    with st.expander("Retrieved document context"):
        st.write(result["context"])