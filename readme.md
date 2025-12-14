# 📦 Local Inventory Demand Balancer

A Python-based inventory optimization system that uses machine learning forecasting and linear programming to balance supply and demand, minimizing costs while maintaining safety stock levels.

## Features

- **Synthetic Data Generation**: Creates realistic sales data with seasonality and trends
- **Demand Forecasting**: Uses Facebook Prophet for accurate time series predictions
- **Inventory Optimization**: Employs linear programming (PuLP with HiGHS solver) to minimize ordering costs
- **Interactive Dashboard**: Streamlit-based visualization of forecasts and optimized reorder plans
- **Safety Stock Management**: Maintains minimum inventory levels based on demand variability

## Prerequisites

- Python 3.8+
- macOS (with Apple Silicon support via HiGHS solver)

## Installation

1. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install pandas numpy prophet pulp highspy joblib streamlit
```

## Usage

### 1. Generate Synthetic Sales Data
```bash
python data_generator.py
```
This creates `synthetic_sales.csv` with 2 years of daily sales data.

### 2. Train Forecast Model
```bash
python forecast.py
```
This trains a Prophet model and generates 30-day forecasts, saving the model to `models/forecast.pkl` and forecasts to `forecast_output.csv`.

### 3. Run Inventory Optimization
```bash
python optimizer.py
```
This solves the linear programming problem to minimize ordering costs while maintaining safety stock, outputting the optimized plan to `optimized_plan.csv`.

### 4. Launch Dashboard
```bash
streamlit run dashboard.py
```
Open the provided URL in your browser to view interactive charts of forecasts and optimized inventory plans.

## Project Structure

```
inventory_balancer/
├── data_generator.py      # Synthetic sales data generation
├── forecast.py           # Prophet forecasting model
├── optimizer.py          # Linear programming optimization
├── dashboard.py          # Streamlit visualization
├── models/               # Saved ML models
│   └── forecast.pkl
├── synthetic_sales.csv   # Generated sales data
├── forecast_output.csv   # Forecast predictions
├── optimized_plan.csv    # Optimization results
└── README.md
```

## Dependencies

- `pandas` - Data manipulation
- `numpy` - Numerical computations
- `prophet` - Time series forecasting
- `pulp` - Linear programming
- `highspy` - HiGHS solver (Apple Silicon compatible)
- `joblib` - Model serialization
- `streamlit` - Web dashboard
- `matplotlib` - Plotting

## Configuration

Key parameters can be adjusted in the code:

- **Safety Stock**: `z = 1.65` (95% service level), `lead_time = 5` days in `optimizer.py`
- **Initial Inventory**: `initial_inventory = 300` units in `optimizer.py`
- **Unit Cost**: `unit_cost = 50` in `optimizer.py`
- **Forecast Horizon**: `periods=30` days in `forecast.py`

## Troubleshooting

- **Solver Error**: Ensure HiGHS is installed (`pip install highspy`) and imported correctly
- **Missing Data**: Run `data_generator.py` and `forecast.py` before optimization
- **Dashboard Issues**: Make sure all CSV files exist before running the dashboard

## License

MIT License
