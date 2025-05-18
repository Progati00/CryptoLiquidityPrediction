# Low-Level Design (LLD)

## Data Preprocessing
- Remove null values
- Normalize features (price, volume, etc.)
- Feature Engineering: Moving averages, volatility, momentum

## Model
- Algorithm: Random Forest Regressor
- Evaluation: R² score, MSE

## Flask App (`app.py`)
- `/`: Home route with input form
- `/predict`: POST route to collect input and return prediction

## File Structure
- `notebooks/`: EDA and training
- `src/`: Flask app
- `models/`: Saved model
- `data/`: Cleaned dataset
