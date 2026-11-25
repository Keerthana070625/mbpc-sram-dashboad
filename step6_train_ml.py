import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

data = pd.read_csv("synthesized_ppa.csv")

features = ["num_banks", "depth_per_bank", "data_width"]
X = data[features]

models = {}
for target in ["area", "delay_ps", "power_mw"]:
    y = data[target]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    preds = model.predict(X)
    mae = mean_absolute_error(y, preds)
    models[target] = model
    print(f"Trained {target} model | Training MAE: {mae:.4f}")

# Test prediction on a new 128-bit config: 4 banks x 8 depth x 4 width = 128 bits
sample = pd.DataFrame([{"num_banks": 4, "depth_per_bank": 8, "data_width": 4}])
print("\nSample Prediction for 4 banks (8x4):")
for target, model in models.items():
    print(f"  Predicted {target}: {model.predict(sample)[0]:.4f}")
    