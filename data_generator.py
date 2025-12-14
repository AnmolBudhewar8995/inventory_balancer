# data_generator.py
import numpy as np
import pandas as pd
from datetime import timedelta, datetime

def generate_sales(n_days=730):
    start = datetime(2023,1,1)
    dates = [start + timedelta(days=i) for i in range(n_days)]

    # base demand + seasonality + noise
    base = 50 + np.sin(np.arange(n_days)/7)*5
    trend = np.linspace(0, 15, n_days)
    noise = np.random.normal(0, 5, n_days)
    
    sales = (base + trend + noise).clip(10, None)

    df = pd.DataFrame({
        "date": dates,
        "sales": sales.astype(int)
    })
    df.to_csv("synthetic_sales.csv", index=False)
    print("Saved → synthetic_sales.csv")

if __name__ == "__main__":
    generate_sales()
