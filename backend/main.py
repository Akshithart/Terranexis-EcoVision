from fastapi import FastAPI, File, UploadFile
from carbon_calculator import carbon_saved
from revenue_calculator import revenue
from sustainability_score import score
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

    waste_type = "Plastic"
    carbon = carbon_saved(waste_type)
    revenue_generated = revenue(waste_type)
    sustainability_score = score(waste_type)

    return {
        "waste_type": waste_type,
        "carbon_saved_kg": carbon,
        "revenue_generated": revenue_generated,
        "sustainability_score": sustainability_score
    }