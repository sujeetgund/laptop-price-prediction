# 💻 Laptop Price Prediction

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green.svg)
![Dockerized](https://img.shields.io/badge/Docker-Supported-blue.svg?logo=docker&logoColor=white)
[![Open Issues](https://img.shields.io/github/issues/sujeetgund/laptop-price-prediction)](https://github.com/sujeetgund/laptop-price-prediction/issues)
[![Last Commit](https://img.shields.io/github/last-commit/sujeetgund/laptop-price-prediction)](https://github.com/sujeetgund/laptop-price-prediction)

Predict laptop prices using machine learning and insightful data analysis


## 🚀 Overview

Welcome to the Laptop Price Predictor — a machine learning project that aims to estimate the market price of a laptop based on its specifications. With the rapid evolution of laptop technology and ever-changing prices, this tool helps identify the key features that influence pricing and uses those insights to build a robust price prediction model.

Whether you're a data scientist, ML engineer, or tech enthusiast, this project offers a clean, modular, and deployable ML pipeline backed by FastAPI and Docker.


## 📌 Problem Statement

Given the specifications of a laptop — such as brand, screen resolution, CPU, RAM, storage, GPU, and weight — can we accurately predict its market price?

By addressing this, we aim to:
- Understand the primary drivers of laptop pricing.
- Engineer meaningful features to improve model performance.
- Deliver a prediction API ready for deployment.


## 🎯 Objectives

- ✅ Clean and preprocess raw laptop specification data.
- ✅ Visualize distributions and discover feature relationships.
- ✅ Engineer new predictive features like pixel density and total storage.
- ✅ Handle missing values, outliers, and inconsistent encodings.
- ✅ Train and evaluate a regression model.
- ✅ Package the trained model into a FastAPI-based prediction service.
- ✅ Provide a Docker-ready environment for easy deployment.


## 📊 Dataset
**Source:** (e.g. Kaggle “Laptop Price” dataset)  
**Size:** ~1,300 records × 12 columns

| Column             | Type      | Description                                                     |
|--------------------|-----------|-----------------------------------------------------------------|
| `Company`          | Categorical | Manufacturer (e.g., Apple, HP, Dell)                          |
| `TypeName`         | Categorical | Laptop category (Ultrabook, Notebook, Gaming, etc.)           |
| `Inches`           | Numeric     | Screen diagonal size (in inches)                              |
| `ScreenResolution` | Categorical | Screen specs with resolution (e.g., “Full HD 1920x1080”)      |
| `Cpu`              | Categorical | Processor model and base clock (e.g., “Intel Core i5 2.3GHz”) |
| `Ram`              | Categorical | Amount of system memory (e.g., “8GB”)                         |
| `Memory`           | Categorical | Storage type & capacity (e.g., “256GB SSD”, “1TB HDD”)        |
| `Gpu`              | Categorical | Graphics card model                                           |
| `OpSys`            | Categorical | Operating system installed                                    |
| `Weight`           | Numeric     | Device weight in kilograms (e.g., “1.37kg”)                   |
| `Price`            | Numeric     | Price in INR (target variable)                                |


## 🗂️ Project Structure

```
laptop-price-predictor/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── run_api.py                   # Entry point for FastAPI app
├── Dockerfile                   # Dockerfile for deployment
├── sample_deploy.ps1            # Sample deploy file with Google Cloud CLI
│
├── app/                         # Main app code (FastAPI & ML logic)
│   ├── __init__.py
│   ├── api/                     # FastAPI routes
│   │   ├── __init__.py
│   │   └── v1/                  # API versioning
│   │       ├── __init__.py
│   │       └── endpoints.py     # FastAPI route definitions
│   │
│   ├── core/                    # Core config (constants, logging, etc.)
│   │   ├── __init__.py
│   │   └── config.py
│   │
│   ├── models/                  # ML model logic
│   │   ├── __init__.py
│   │   └── predictor.py         # Load and use model for prediction
│   │
│   ├── schemas/                 # Pydantic request/response models
│   │   ├── __init__.py
│   │   └── laptop.py
│   │
│   └── utils/                   # Helper functions (e.g., preprocessing)
│       ├── __init__.py
│       └── preprocessing.py
│
├── research/                    # Exploratory notebooks & research
│   ├── assets/
│   ├── data/
│   ├── model/
│   ├── processed_data/
│   ├── eda.ipynb
│   ├── model_training.ipynb
│   └── insights.md
```

**🔍 Key Components:**

* `app/api/v1/endpoints.py`: FastAPI routes for prediction API.
* `models/predictor.py`: Loads and runs the trained model.
* `utils/preprocessing.py`: Data cleaning and feature engineering logic.
* `research/eda.ipynb`: Exploratory data analysis.
* `research/model_training.ipynb`: Model training & evaluation.
* `run_api.py`: FastAPI entry point.
* `Dockerfile`: Containerization for scalable deployment.


## ⚙️ Getting Started

### 🔧 Requirements

```bash
pip install -r requirements.txt
```

### 🏃 Run the API

```bash
uvicorn run_api:app --reload --port 8080
```

Then navigate to: [http://localhost:8080/docs](http://localhost:8000/docs)

### 🐳 Docker Support

Build and run the app inside Docker:
```bash
docker build -t laptop-price-predictor .
docker run -p 8080:8080 laptop-price-predictor
```


## 🌐 API Endpoint

| Method | Endpoint   | Description                 |
| ------ | ---------- | --------------------------- |
| GET   | `/info` | Get information about app |
| POST   | `/predict` | Predicts price for a laptop |


**Sample request:**

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Company": "Asus",
  "TypeName": "Notebook",
  "Inches": 15.6,
  "Ram": 8,
  "OpSys": "Windows 10",
  "Weight": 1.69,
  "HasIpsPanel": 1,
  "HasTouchScreen": 0,
  "ResWidth": 1920,
  "ResHeight": 1080,
  "ResCategory": "High",
  "Ppi": 141.21,
  "Ssd": 512,
  "Hdd": 0,
  "Flash": 0,
  "Hybrid": 0,
  "CpuCategory": "Intel Core i3",
  "CpuSpeedGhz": 1,
  "GpuCategory": "Intel Low-End"
}'
```


## 📈 Insights

Key findings during EDA and modeling can be found in [research/insights.md](research/insights.md). Some highlights:
- High-resolution displays and SSDs tend to increase price.
- GPU and CPU models are strong price indicators.
- RAM size impacts pricing, especially when paired with high-end components.


## 📜 License

This project is licensed under the MIT License.