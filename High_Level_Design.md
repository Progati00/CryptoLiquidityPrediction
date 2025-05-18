# High-Level Design (HLD)

## Objective
To predict the liquidity of cryptocurrencies using a machine learning model trained on historical data.

## System Overview
- Data Collection from CSV
- Data Preprocessing and Feature Engineering
- Model Training (Random Forest or similar)
- Flask Web App for Prediction

## Components
1. Jupyter Notebook (`notebooks/`): For EDA, preprocessing, and training
2. Flask App (`src/app.py`): For deployment
3. Trained Model (`models/best_model.joblib`)
4. Data Files (`data/`)
