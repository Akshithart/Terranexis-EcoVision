def revenue(waste_type, weight):

    price = {
        "Plastic Bottle":0.02,
        "Paper":0.01,
        "Metal Can":0.05,
        "Glass Bottle":0.01
    }

    return round(weight * price.get(waste_type,0),2)