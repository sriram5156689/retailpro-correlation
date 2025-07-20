from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io
import re

app = FastAPI()

@app.post("/captcha")
async def captcha_solver(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))

    # OCR (extract text)
    text = pytesseract.image_to_string(image)

    # Match 8-digit × 8-digit multiplication
    match = re.search(r"(\d{8})\s*[*xX×]\s*(\d{8})", text)
    if not match:
        return JSONResponse(status_code=400, content={"error": "Could not detect multiplication"})

    num1 = int(match.group(1))
    num2 = int(match.group(2))
    result = num1 * num2

    return {
        "answer": result,
        "email": "23f2002842@ds.study.iitm.ac.in"
    }
