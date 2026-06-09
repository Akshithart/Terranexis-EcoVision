from unittest import result

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from carbon_calculator import carbon_saved
from revenue_calculator import revenue
from sustainability_score import score
from ai.detector import detect_waste
from weight_estimator import estimate_weight
from recommendation import recommendation
import os
import os
from dotenv import load_dotenv

load_dotenv()



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Terranexis EcoVision API is running"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    return {
        "filename": file.filename
    }

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    os.makedirs("uploads", exist_ok=True)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = detect_waste(file_path)

    waste_type = result["waste_type"]
    confidence = result["confidence"]
    if "Plastic" in waste_type:
        waste_type = "Plastic Bottle"
    elif "Metal" in waste_type:
        waste_type = "Metal Can"
    elif "Glass" in waste_type:
        waste_type = "Glass Bottle"
    elif "Paper" in waste_type:
        waste_type = "Paper"
    else:
        waste_type = "Organic"
    weight = estimate_weight(waste_type)

    carbon = carbon_saved(
        waste_type,
        weight
    )

    money = revenue(
        waste_type,
        weight
    )

    eco_score = score(waste_type)
    suggestion = recommendation(
    waste_type
)
    
    return {
        "waste_type": waste_type,
        "confidence": confidence,
        "estimated_weight": weight,
        "carbon_saved": carbon,
        "revenue": money,
        "sustainability_score": eco_score,
        "suggestion": suggestion
    }