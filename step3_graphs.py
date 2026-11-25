import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("baseline_data.csv")

metrics = ["Area", "Delay_ps", "Total_Power_W"]
titles = [
    "Area Comparison (Lower is Better)",
    "Data Path Delay in ps (Lower is Better)",
    "Total Power in W (Lower is Better)",
]

# Create 3 side-by-side charts
fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for ax, col, title in zip(axes, metrics, titles):
    ax.bar(df["Architecture"], df[col])
    ax.set_title(title)
    ax.set_ylabel(col)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("baseline_comparison.png", dpi=300)
plt.show() 