import os
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Paths
DATA_PATH = "data/processed/california_housing_processed.csv"
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# Load processed data
df = pd.read_csv(DATA_PATH)
X = df.drop("target", axis=1)
y = df["target"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# MLflow tracking setup
mlflow.set_tracking_uri("file://" + os.path.abspath("mlruns"))
mlflow.set_experiment("California Housing Regression")

models = {
    "LinearRegression": LinearRegression(),
    "DecisionTree": DecisionTreeRegressor(random_state=42)
}

best_rmse = float("inf")
best_model_name = None
best_model = None

for name, model in models.items():
    with mlflow.start_run(run_name=name):
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        rmse = mean_squared_error(y_test, preds, squared=False)

        mlflow.log_param("model_name", name)
        mlflow.log_metric("rmse", rmse)
        mlflow.sklearn.log_model(model, name)

        print(f"{name} RMSE: {rmse:.4f}")

        if rmse < best_rmse:
            best_rmse = rmse
            best_model_name = name
            best_model = model

# Save best model
joblib.dump(best_model, os.path.join(MODEL_DIR, "best_model.pkl"))
print(f"Best model: {best_model_name} with RMSE: {best_rmse:.4f}")
