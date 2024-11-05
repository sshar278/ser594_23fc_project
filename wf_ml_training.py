# wf_ml_training.py
"""
This script is responsible for training the machine learning models.
Steps:
1. Load processed data from the 'data_processed' folder.
2. Split the data into features and target variables.
3. Train a RandomForestClassifier model on the training data.
4. Save the trained model to the 'models' folder for later use.
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Paths
DATA_PROCESSED_PATH = "data_processed/processed_data.csv"
MODELS_PATH = "models"
MODEL_FILE = os.path.join(MODELS_PATH, "election_rf_model.pkl")

# Ensure the models directory exists
os.makedirs(MODELS_PATH, exist_ok=True)

# Load the processed data
data = pd.read_csv(DATA_PROCESSED_PATH)

# Feature selection and train-test split
X = data.drop(columns=['target'])  # Replace 'target' with the actual target column name
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, MODEL_FILE)

print(f"Model trained and saved to {MODEL_FILE}")

