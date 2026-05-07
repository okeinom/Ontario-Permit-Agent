def classify_structure(description: str) -> str:
    text = description.lower()

    if "shed" in text:
        return "shed / accessory structure"

    if "cabin" in text:
        return "cabin / small building"

    if "garage" in text:
        return "garage / accessory structure"

    if "deck" in text:
        return "deck"

    return "unknown structure type"