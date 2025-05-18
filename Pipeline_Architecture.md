# Pipeline Architecture

1. **Data Loading**
   - Read dataset from CSV in `data/`

2. **Preprocessing**
   - Clean missing values
   - Feature scaling and transformation

3. **Feature Engineering**
   - Add MA7, volatility, momentum, etc.

4. **Model Training**
   - Train and validate using cross-validation
   - Save model to `models/best_model.joblib`

5. **Deployment**
   - Load model in Flask app
   - Accept user input and return prediction
