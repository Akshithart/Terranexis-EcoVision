def score(waste):

    scores = {
        "Plastic":85,
        "Paper":90,
        "Metal":95,
        "Glass":88,
        "Organic":92
    }

    return scores.get(waste,75)