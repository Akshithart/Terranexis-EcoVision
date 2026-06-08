import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AQ.Ab8RN6JSqeroGztCioy4-878SbPhP6BRYXKoAOKThkR3IWy8qA")

model = genai.GenerativeModel("gemini-2.5-flash")

def detect_waste(image_path):

    image = Image.open(image_path)

    response = model.generate_content([
        """
        Identify this waste item.

        Return only:
        Plastic
        Paper
        Metal
        Glass
        Organic
        E-Waste
        """,
        image
    ])

    waste_type = response.text.strip()

    return {
        "waste_type": waste_type,
        "confidence": 90
    }