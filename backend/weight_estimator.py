def estimate_weight(waste_type):

    weights = {
        "Plastic Bottle": 20,
        "Paper": 15,
        "Metal Can": 35,
        "Glass Bottle": 150
    }

    return weights.get(waste_type, 10)