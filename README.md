# CryptoLiquidityPrediction


# 🪙 Crypto Liquidity Prediction

This project predicts the liquidity ratio of cryptocurrencies using machine learning techniques.

---

## 📁 Project Structure

```

CryptoLiquidityPrediction/
├── data/                  # Contains raw/cleaned cryptocurrency CSV data
├── docs/                  # Design documents: HLD, LLD, Architecture, Final Report
├── models/                # Trained machine learning model (best\_model.joblib)
├── notebooks/             # Jupyter Notebook with EDA, preprocessing, model training
├── src/                   # Flask application (app.py for API deployment)

````

---

## 📌 Project Overview

This project aims to forecast the liquidity ratio of cryptocurrencies using supervised machine learning. It includes:

- Data preprocessing
- Model selection using `GridSearchCV`
- Performance evaluation
- Deployment of a prediction API using Flask

---

## 🛠️ Technologies Used

- Python 3
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib
- Flask
- Jupyter Notebook

---

## 🤖 Machine Learning Details

- **Model Used:** Random Forest Regressor with GridSearchCV  
- **Target Variable:** Liquidity Ratio  
- **Evaluation Metrics:** R² Score, RMSE, MAE  

The trained model is saved here: `models/best_model.joblib`

---

## 🚀 How to Run the Project

### 1. Run Jupyter Notebook (for analysis & training)

```bash
cd notebooks
jupyter notebook Cryptocurrency_ML_Project.ipynb
````

### 2. Run Flask App (for prediction API)

```bash
cd src
python app.py
```

Then open your browser and go to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📄 Reports & Documentation

You can find detailed documentation inside the `docs/` folder:

* `HLD.md` – High-Level Design
* `LLD.md` – Low-Level Design
* `Pipeline_Architecture.md` – Pipeline & Flow
* `Final_Report.md` – Final summary & analysis

---

## 👤 Author

**Progati Podder**
🔗 [GitHub Profile](https://github.com/Progati00)
