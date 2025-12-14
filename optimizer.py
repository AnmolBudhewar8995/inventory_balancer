# optimizer.py
import pandas as pd
import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, HiGHS

def compute_safety_stock(df):
    std = df['sales'].std()
    lead_time = 5  # days
    z = 1.65       # 95% service level
    ss = int(z * std * np.sqrt(lead_time))
    return ss

def optimize_inventory():
    forecast = pd.read_csv("forecast_output.csv")
    future = forecast.tail(30)  # next 30 days
    demand = future['yhat'].values

    safety_stock = compute_safety_stock(pd.read_csv("synthetic_sales.csv"))

    days = len(demand)
    unit_cost = 50

    # LP model
    model = LpProblem("InventoryOptimizer", LpMinimize)

    order_qty = LpVariable.dicts("order_qty", range(days), lowBound=0)
    inventory = LpVariable.dicts("inventory", range(days), lowBound=0)

    # Initial inventory
    initial_inventory = 300

    # Constraints per day
    for d in range(days):
        if d == 0:
            model += inventory[d] == initial_inventory + order_qty[d] - demand[d]
        else:
            model += inventory[d] == inventory[d-1] + order_qty[d] - demand[d]

        # Maintain safety stock
        model += inventory[d] >= safety_stock

    # Objective: minimize cost
    model += lpSum(order_qty[d] * unit_cost for d in range(days))

    model.solve(HiGHS())

    print("Status:", LpStatus[model.status])

    results = []
    for d in range(days):
        results.append({
            "day": d+1,
            "forecasted_demand": demand[d],
            "order_qty": order_qty[d].value(),
            "inventory_end": inventory[d].value(),
        })

    df_opt = pd.DataFrame(results)
    df_opt.to_csv("optimized_plan.csv", index=False)
    print("Saved → optimized_plan.csv")

if __name__ == "__main__":
    optimize_inventory()
