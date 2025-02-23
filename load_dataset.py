import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Combined Data.csv")

# Drop 'Unnamed: 0' column if it exists
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Drop missing values from the 'statement' column
df = df.dropna(subset=["statement"])

# Save the cleaned dataset
df.to_csv("dataset/cleaned_data.csv", index=False)

print("✅ Dataset cleaned and saved as 'dataset/cleaned_data.csv'")


# Load the cleaned dataset
df = pd.read_csv("dataset/cleaned_data.csv")

# Check label distribution
print(df["status"].value_counts())
