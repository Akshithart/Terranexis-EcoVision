def carbon_saved(waste_type, weight):

    factor = {
        "Plastic Bottle": 0.006,
        "Paper": 0.004,
        "Metal Can": 0.009,
        "Glass Bottle": 0.002
    }

    return round(weight * factor.get(waste_type,0),2)