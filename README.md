# Laptop Price Prediction


## 1. Problem Statement
We want to understand which factors most influence the selling price of a laptop.  
Given a set of characteristics (brand, screen size & resolution, processor, RAM, storage type & size, GPU, operating system, weight), our goal is to build insights and ultimately a predictive model that can estimate the market price of a laptop.

---

## 2. Objective
- Perform data cleaning and feature engineering to prepare the data for modeling.  
- Visualize univariate distributions and bivariate relationships to discover patterns and correlations.  
- Identify and handle outliers, missing values, or inconsistent feature encodings.  
- Generate new features (e.g., pixel count from screen resolution, storage total capacity, CPU speed) that may improve predictive power.  
- Summarize key findings to guide the choice of modeling techniques in downstream tasks.

---

## 3. Dataset Description
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

---

## 4. Project Structure

**Complete Project Structure:**

```
laptop-price-predictor/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── run_api.py                   # Entry point for FastAPI app
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

**Description of Key Directories and Files:**

* `.gitignore`: Specifies intentionally untracked files that Git should ignore.
* `LICENSE`: Contains the licensing information for the project.
* `README.md`: This file, providing an overview of the project.
* `requirements.txt`: Lists the Python dependencies required to run the project.
* `run_api.py`: The main script to start the FastAPI application.
* `app/`: Contains the core application logic.
    * `api/`: Handles the API routing using FastAPI.
        * `v1/`: Directory for version 1 of the API endpoints.
            * `endpoints.py`: Defines the different API endpoints.
    * `core/`: Contains core configuration files.
        * `config.py`: Holds configuration settings for the application.
    * `models/`: Houses the machine learning model related logic.
        * `predictor.py`: Responsible for loading the trained ML model and making predictions.
    * `schemas/`: Defines the data structures for request and response bodies using Pydantic.
        * `laptop.py`: Defines the schema for laptop data.
    * `utils/`: Contains utility functions.
        * `preprocessing.py`: Includes functions for data preprocessing.
* `research/`: Contains files related to the exploratory data analysis and model development process.
    * `assets/`: Contain any static assets generated in notebooks.
    * `data/`: Stores the raw dataset used for training.
    * `model/`: Contain the serialized trained machine learning model from notebooks.
    * `processed_data/`: Store intermediate or processed datasets.
    * `eda.ipynb`: Jupyter Notebook for exploratory data analysis.
    * `model_training.ipynb`: Jupyter Notebook for training the machine learning model.
    * `insights.md`: Markdown file documenting insights gained during the research phase.

---