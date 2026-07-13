from fastapi import FastAPI
from app.utils.validation import validate_schema_consistency
from app.utils.model_helper import predict

app = FastAPI(title= "Fraud Prediction API")

@app.get("/")
def root():
    return{"message": "Fraud Prediction API is running"}

@app.post("/predict")
def predict_endpoint(request:list[dict]):
    is_valid, msg_error, data = validate_schema_consistency(request)
    if is_valid:
        result = predict(data)
        return {"prediction": result}