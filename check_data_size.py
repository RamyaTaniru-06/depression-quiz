import pandas as pd

# Check original cleaned dataset
df_cleaned = pd.read_csv("dataset/final_cleaned_data.csv")
print(f"Original dataset size: {df_cleaned.shape}")

# Check vectorized data
X = pd.read_csv("dataset/vectorized_data.csv")
print(f"Vectorized dataset size: {X.shape}")
