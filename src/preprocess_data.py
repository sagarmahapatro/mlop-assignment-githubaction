import pandas as pd
import os

# Load raw data
df = pd.read_csv("data/raw/california_housing.csv")

# Example preprocessing
df = df[df["MedHouseVal"] < 5]  # Remove extreme values
df["AveRooms"] = df["AveRooms"] / df["HouseAge"]

# Ensure folder exists
os.makedirs("data/processed", exist_ok=True)

# Save processed data
df.to_csv("data/processed/california_housing_processed.csv", index=False)

print("✅ Preprocessing complete. Processed file saved.")
