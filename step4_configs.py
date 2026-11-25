
import pandas as pd

configs = [
    # config_name, num_banks, depth_per_bank, data_width
    ("1_bank_16x8", 1, 16, 8),
    ("2_banks_8x8", 2, 8, 8),
    ("4_banks_4x8", 4, 4, 8),
    ("8_banks_2x8", 8, 2, 8),
    ("2_banks_16x4", 2, 16, 4),
    ("4_banks_8x4", 4, 8, 4),
    ("8_banks_4x4", 8, 4, 4),
    ("4_banks_4x8_mbpc4", 4, 4, 8),
]

rows = []
for name, banks, depth, width in configs:
    total_bits = banks * depth * width
    assert total_bits == 128, f"{name} is {total_bits} bits, not 128!"
    rows.append({
        "config_name": name,
        "num_banks": banks,
        "depth_per_bank": depth,
        "data_width": width,
        "total_bits": total_bits,
    })

cfg_df = pd.DataFrame(rows)
cfg_df.to_csv("bank_configs.csv", index=False)
print(cfg_df) 