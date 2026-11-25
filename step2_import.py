import pandas as pd

# Load the CSV table into a 'DataFrame' (think of it as a smart table)
df = pd.read_csv("baseline_data.csv")

print("Here is our SRAM data:")
print(df)
