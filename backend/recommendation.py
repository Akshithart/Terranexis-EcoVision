def recommendation(waste_type):

    data = {

        "Plastic Bottle":
        "Send to plastic recycling center.",

        "Paper":
        "Reuse before recycling.",

        "Metal Can":
        "Sell to local scrap dealer.",

        "Glass Bottle":
        "Return to glass collection unit."
    }

    return data.get(
        waste_type,
        "Dispose responsibly."
    )