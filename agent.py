from tools.rag_tool import search_building_docs
from tools.calculator_tool import calculate_area
from tools.classifier_tool import classify_structure
from tools.checklist_tool import generate_checklist
from llm import generate_answer, generate_tool_plan


def run_permit_agent(
    question: str,
    length: float,
    width: float,
    description: str
) -> dict:
    """
    Simple agent orchestrator.
    Decides which tools to run and returns final result.
    """

    steps = []

    plan = generate_tool_plan(question)
    steps.append(f"Tool plan: {plan}")
    structure_type = None
    project_area = None
    checklist = None

    if "classify_structure" in plan:
        structure_type = classify_structure(description)
        steps.append(f"Classified structure: {structure_type}")
    
    if "calculate_area" in plan:
        project_area = calculate_area(length, width)
        steps.append(f"Calculated area: {project_area['area_sq_ft']} sq ft")
    
    if "search_building_docs" in plan:
        context = search_building_docs(question)
        steps.append("Retrieved document context.")
    else:
        context = ""
    
    if "generate_checklist" in plan:
        checklist = generate_checklist(
            structure_type or "unknown",
            project_area["area_sq_ft"] if project_area else 0
        )
        steps.append("Generated checklist.")
    else:
        checklist = []  

    # Final answer
    answer = generate_answer(
        question,
        context,
        project_area,
        structure_type,
        checklist
    )
    steps.append("Generated final answer using retrieved context and tool outputs.")

    return {
        "answer": answer,
        "steps": steps,
        "structure_type": structure_type,
        "project_area": project_area,
        "checklist": checklist,
        "context": context
    }