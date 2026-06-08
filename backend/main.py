from fastapi import FastAPI, File, UploadFile
from carbon_calculator import carbon_saved
from revenue_calculator import revenue
from sustainability_score import score
from ai.detector import detect_waste
from weight_estimator import estimate_weight


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
  
    weight = estimate_weight(waste_type)
    carbon = carbon_saved(waste_type, weight)

    
    revenue_generated = revenue(waste_type, weight)
    sustainability_score = score(waste_type)

    return {
    "waste_type": waste_type,
    "confidence": confidence,
    "estimated_weight_g": weight,
    "carbon_saved_kg": carbon,
    "revenue_generated": revenue_generated,
    "sustainability_score": sustainability_score
}