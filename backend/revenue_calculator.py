def revenue(waste):

    data = {
        "Plastic":0.4,
        "Paper":0.2,
        "Metal":1.5,
        "Glass":0.3,
        "Organic":0
    }

    return data.get(waste,0)