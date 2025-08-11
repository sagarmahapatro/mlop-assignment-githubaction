from sklearn.datasets import fetch_california_housing
import pandas as pd
import os

# Ensure folder exists
os.makedirs("./data/raw", exist_ok=True)

# Fetch dataset as pandas DataFrame
housing = fetch_california_housing(as_frame=True)

# Combine features and target into a single DataFrame
df = pd.concat([housing.data, housing.target.rename("MedHouseVal")], axis=1)

save_path = os.path.join(".", "data", "raw", "california_housing.csv")
print("Saving to:", os.path.abspath(save_path))  

# Save to CSV
df.to_csv(save_path , index=False)

print("✅ California housing dataset saved to data/raw/california_housing.csv")
