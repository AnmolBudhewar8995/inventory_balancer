# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📦 Local Inventory Demand Balancer")

# Load data
forecast = pd.read_csv("forecast_output.csv").tail(30)
opt = pd.read_csv("optimized_plan.csv")

st.header("📈 30-Day Demand Forecast")
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(forecast['ds'], forecast['yhat'], label="Forecast")
ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], alpha=0.2, label="Confidence")
ax.legend()
st.pyplot(fig)

st.header("📦 Optimized Reorder Plan")
st.dataframe(opt)

st.header("📦 Inventory Trajectory")
fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(opt['day'], opt['inventory_end'], label="Ending Inventory", color='green')
ax2.bar(opt['day'], opt['order_qty'], alpha=0.4, label="Order Qty")
ax2.legend()
st.pyplot(fig2)

st.success("Optimization complete. Use this dashboard to adjust reorder strategy.")
