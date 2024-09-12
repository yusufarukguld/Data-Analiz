from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

@app.post("/upload")
async def create_upload_file(file: UploadFile = File(...)) -> JSONResponse:
    # Dosya pandas DataFrame'e çevriliyor
    print(file)
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file.file)
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(file.file)
    else:
        return JSONResponse(status_code=400, content={"message": "Unsupported file format"})

    # Basit bir istatistik çıkartma
    description = df.describe(include='all').to_json()

    # JSON olarak cevap döndürme
    return JSONResponse(status_code=200, content={"description": description})


def run():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
