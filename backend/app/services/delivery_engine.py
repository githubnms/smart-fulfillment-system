def calculate_delivery(distance: float, priority: str):
    base_cost = distance * 5

    if priority == "fast":
        return {
            "time": max(1, distance / 2),
            "cost": base_cost * 2
        }
    elif priority == "cheap":
        return {
            "time": distance,
            "cost": base_cost
        }
    else:  # balanced
        return {
            "time": distance * 0.75,
            "cost": base_cost * 1.5
        }