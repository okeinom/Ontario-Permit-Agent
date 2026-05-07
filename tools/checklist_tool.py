def generate_checklist(structure_type: str, area_sq_ft: float) -> list[str]:
    checklist = [
        "Confirm local municipality permit requirements.",
        "Check zoning rules such as setbacks, height, and lot coverage.",
        "Confirm whether Ontario Building Code requirements apply.",
        "Prepare a basic site plan.",
        "Prepare drawings showing size, height, and construction details.",
    ]

    if area_sq_ft > 160:
        checklist.append("Because the area is over 160 sq ft, verify permit requirements carefully.")

    if "cabin" in structure_type:
        checklist.append("Confirm whether the structure is considered habitable space.")

    return checklist