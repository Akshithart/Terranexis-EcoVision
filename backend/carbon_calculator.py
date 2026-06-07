def carbon_saved(waste):

    data = {
        "Plastic":0.12,
        "Paper":0.08,
        "Metal":0.30,
        "Glass":0.10,
        "Organic":0.05
    }

    return data.get(waste,0)
