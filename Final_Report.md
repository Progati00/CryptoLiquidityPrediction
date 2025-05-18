# Final Report

## Objective
Build a model to predict cryptocurrency liquidity using historical market data.

## Data Summary
- Source: Preloaded CSV
- Features: Price, volume, volatility, momentum indicators, etc.

## Model Used
- Algorithm: Random Forest Regressor
- Performance:
  - R² Score: 0.87
  - MSE: 0.012

## Key Insights
- Liquidity is strongly influenced by price volatility and volume changes
- Feature engineering (momentum, MA7) improved model accuracy

## Deployment
- Implemented a Flask Web App to test predictions interactively
