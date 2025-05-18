from flask import Flask, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("best_model.joblib")

@app.route('/')
def home():
    return '''
    <h2>Liquidity Ratio Predictor</h2>
    <form method="post" action="/predict">
      Price: <input name="price"><br>
      1h Change: <input name="h1"><br>
      24h Change: <input name="h24"><br>
      7d Change: <input name="d7"><br>
      24h Volume: <input name="volume"><br>
      Market Cap: <input name="mkt_cap"><br>
      Liquidity Ratio: <input name="liq_ratio"><br>
      Weekly Volatility: <input name="volatility"><br>
      Price MA7: <input name="price_ma"><br>
      Volume MA7: <input name="volume_ma"><br>
      Price Volatility 7d: <input name="price_vol"><br>
      Liquidity Momentum 1d: <input name="liq_mom1"><br>
      Liquidity Momentum 7d: <input name="liq_mom7"><br>
      <input type="submit">
    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input from form
        features = [
            float(request.form['price']),
            float(request.form['h1']),
            float(request.form['h24']),
            float(request.form['d7']),
            float(request.form['volume']),
            float(request.form['mkt_cap']),
            float(request.form['liq_ratio']),
            float(request.form['volatility']),
            float(request.form['price_ma']),
            float(request.form['volume_ma']),
            float(request.form['price_vol']),
            float(request.form['liq_mom1']),
            float(request.form['liq_mom7']),
        ]
        features = np.array([features])

        # Make prediction
        prediction = model.predict(features)[0]
        return f'<h3>Predicted Liquidity Ratio: {prediction:.4f}</h3>'
    except Exception as e:
        return f"<h3>Error: {e}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
