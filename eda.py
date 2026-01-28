import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("quotes_data.csv")

# Basic EDA
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nAuthor count:")
print(df["author"].value_counts().head())

# Visualization
author_counts = df["author"].value_counts().head(10)

author_counts.plot(kind="bar")
plt.title("Top 10 Authors by Quote Count")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.tight_layout()
plt.show()
