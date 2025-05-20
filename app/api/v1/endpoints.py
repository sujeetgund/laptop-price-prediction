from fastapi import APIRouter
from app.schemas.laptop import Laptop, PriceOutput
from app.models.predictor import predict_price

router = APIRouter()


@router.get("/info")
def get_info():
    return {
        "name": "Laptop Price Predictor",
        "version": "1.0.0",
        "description": "Predicts the price of a laptop based on its specifications.",
        "github_repo": "https://github.com/sujeetgund/laptop-price-prediction",
        "author": "Sujeet Gund",
        "author_email": "sujeetgund@gmail.com",
    }


@router.post("/predict", response_model=PriceOutput)
def predict(data: Laptop):
    price = predict_price(data)
    return {"predicted_price": price}
