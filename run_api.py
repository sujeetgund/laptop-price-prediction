from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router

app = FastAPI(title="Laptop Price Predictor API")
app.include_router(api_router)