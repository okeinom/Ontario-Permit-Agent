def calculate_area(length_ft: float, width_ft: float) -> dict:
    area = length_ft * width_ft

    return {
        "length_ft": length_ft,
        "width_ft": width_ft,
        "area_sq_ft": area,
        "area_sq_m": round(area * 0.092903, 2),
    }