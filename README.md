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