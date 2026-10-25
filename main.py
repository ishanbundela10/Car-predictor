from fastapi import FastAPI
from schema import CarFeatures, PredictionResponse
from model import predict_price, load_artifacts
from fastapi.responses import JSONResponse

app = FastAPI(title="Car Prediction API", version="1.4.5")

@app.on_event("startup")
def startup_event():
    load_artifacts()

@app.get("/")
def test():
    return JSONResponse(status_code=200, content={"SUCCESS" : True, "message": "this is test route"})

@app.post("/predict", response_model=PredictionResponse)
def predict(features: CarFeatures):
    price = predict_price(features.model_dump())
    return PredictionResponse(prediction_price=price)