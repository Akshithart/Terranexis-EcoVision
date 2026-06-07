from fastapi import FastAPI, File, UploadFile
from carbon_calculator import carbon_saved
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

    return {
        "waste_type": waste_type,
        "carbon_saved_kg": carbon
    }