# forecast.py
import pandas as pd
from prophet import Prophet
import joblib
from pathlib import Path

def train_forecast():
    df = pd.read_csv("synthetic_sales.csv")
    df = df.rename(columns={"date": "ds", "sales": "y"})

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    Path("models").mkdir(exist_ok=True)
    joblib.dump(model, "models/forecast.pkl")
    print("Model saved → models/forecast.pkl")

    forecast[['ds','yhat','yhat_lower','yhat_upper']].to_csv("forecast_output.csv", index=False)
    print("Forecast saved → forecast_output.csv")

if __name__ == "__main__":
    train_forecast()
