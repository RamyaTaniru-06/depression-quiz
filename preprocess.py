import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv("dataset/cleaned_data.csv")

# Check if data is loaded
print(df.head())

# Test a single row for text cleaning
nltk.download("stopwords")

def clean_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text = " ".join(word for word in text.split() if word not in stopwords.words("english"))
    return text

# Apply text cleaning on a small sample
df["cleaned_statement"] = df["statement"].head(10).apply(clean_text)

# Print results
print(df[["statement", "cleaned_statement"]])
# Remove rows with missing cleaned_statement values
df = df.dropna(subset=["cleaned_statement"])

# Save cleaned dataset
df.to_csv("dataset/final_cleaned_data.csv", index=False)

# Check if NaNs are removed
print(df.isnull().sum())
print(df.head())
