from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from app.predict import predict_image

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Image classification backend running"}

@app.post("/classify")
async def classify(file: UploadFile = File(...)):

    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    result = predict_image(image)

    return result
