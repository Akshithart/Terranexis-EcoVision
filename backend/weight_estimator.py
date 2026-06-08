def estimate_weight(waste_type):

    weights = {
        "Plastic":20,
        "Paper":15,
        "Metal":35,
        "Glass":150,
        "Organic":100,
        "E-Waste":250
    }

    return weights.get(waste_type,50)