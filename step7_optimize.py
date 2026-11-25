import pandas as pd
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("synthesized_ppa.csv")
features = ["num_banks", "depth_per_bank", "data_width"]

models = {}
for target in ["area", "delay_ps", "power_mw"]:
    m = RandomForestRegressor(n_estimators=100, random_state=42)
    m.fit(data[features], data[target])
    models[target] = m

# Generate all valid 128-bit combinations where num_banks * depth_per_bank * data_width == 128
candidates = []
for banks in [1, 2, 4, 8, 16]:
    for depth in [1, 2, 4, 8, 16, 32]:
        for width in [4, 8, 16, 32]:
            if banks * depth * width == 128:
                candidates.append({
                    "num_banks": banks,
                    "depth_per_bank": depth,
                    "data_width": width,
                })

cand_df = pd.DataFrame(candidates).drop_duplicates()
cand_df["pred_area"] = models["area"].predict(cand_df[features])
cand_df["pred_delay_ps"] = models["delay_ps"].predict(cand_df[features])
cand_df["pred_power_mw"] = models["power_mw"].predict(cand_df[features])

# Normalize each metric (0 = lowest/best, 1 = highest/worst)
for col in ["pred_area", "pred_delay_ps", "pred_power_mw"]:
    rng = cand_df[col].max() - cand_df[col].min()
    cand_df[col + "_norm"] = (cand_df[col] - cand_df[col].min()) / (rng if rng > 0 else 1)

# Weights (adjust if you prioritize power or delay more)
w_area, w_delay, w_power = 0.25, 0.35, 0.40
cand_df["ppa_score"] = (
    w_area * cand_df["pred_area_norm"]
    + w_delay * cand_df["pred_delay_ps_norm"]
    + w_power * cand_df["pred_power_mw_norm"]
)

best_configs = cand_df.sort_values("ppa_score").head(5)
print("Top 5 Recommended 128-bit Configurations (Lower PPA Score is Better):")
print(best_configs[["num_banks", "depth_per_bank", "data_width", "pred_area", "pred_delay_ps", "pred_power_mw", "ppa_score"]].to_string(index=False))