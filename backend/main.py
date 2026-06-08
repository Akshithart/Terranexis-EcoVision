from fastapi import FastAPI, File, UploadFile
from carbon_calculator import carbon_saved
from revenue_calculator import revenue
from sustainability_score import score
from ai.detector import detect_waste

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Terranexis EcoVision API is running"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    return {
        "filename": file.filename
    }

@app.post("/analyze")
async def analyze_image():

    result = detect_waste("sample.jpg")

    waste_type = result["waste_type"]
    confidence = result["confidence"]

    if "Plastic" in waste_type:
        waste_type = "Plastic"
    elif "Paper" in waste_type:
        waste_type = "Paper"
    elif "Metal" in waste_type:
        waste_type = "Metal"
    elif "Glass" in waste_type:
        waste_type = "Glass"
    elif "Organic" in waste_type:
        waste_type = "Organic"
    else:
        waste_type = "Other"

    carbon = carbon_saved(waste_type)
    revenue_generated = revenue(waste_type)
    sustainability_score = score(waste_type)

    return {
        "waste_type": waste_type,
        "confidence": confidence,
        "carbon_saved_kg": carbon,
        "revenue_generated": revenue_generated,
        "sustainability_score": sustainability_score
    }