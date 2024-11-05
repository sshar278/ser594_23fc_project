# wf_ml_evaluation.py
"""
This script is responsible for splitting the data, training the model, making predictions, and evaluating its performance.
Steps:
1. Load processed data and split into training and test sets.
2. Save the training and test sets for further use.
3. Train the model by calling functions from the training script.
4. Use the trained model to make predictions by calling functions from the prediction script.
5. Evaluate the model's performance using classification metrics.
6. Save the evaluation report to a text file.
"""

import os
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import joblib

# Paths
DATA_PROCESSED_PATH = "data_processed/processed_data.csv"
MODELS_PATH = "models"
EVALUATION_PATH = "evaluation"
TRAIN_DATA_FILE = os.path.join(MODELS_PATH, "train_data.csv")
TEST_DATA_FILE = os.path.join(MODELS_PATH, "test_data.csv")
MODEL_FILE = os.path.join(MODELS_PATH, "election_rf_model.pkl")
EVALUATION_REPORT_FILE = os.path.join(EVALUATION_PATH, "evaluation_report.txt")

# Ensure the models and evaluation directories exist
os.makedirs(MODELS_PATH, exist_ok=True)
os.makedirs(EVALUATION_PATH, exist_ok=True)

# Load the processed data
data = pd.read_csv(DATA_PROCESSED_PATH)

# Split data into training and test sets
X = data.drop(columns=['target'])  # Replace 'target' with the actual target column name
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save train and test sets
train_data = pd.concat([X_train, y_train], axis=1)
train_data.to_csv(TRAIN_DATA_FILE, index=False)

test_data = pd.concat([X_test, y_test], axis=1)
test_data.to_csv(TEST_DATA_FILE, index=False)

# Train the model
import wf_ml_training

# Load the trained model
model = joblib.load(MODEL_FILE)

# Make predictions
import wf_ml_prediction

# Evaluate the model on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy}")
print("Classification Report:\n", report)

# Save the evaluation report to a text file
with open(EVALUATION_REPORT_FILE, "w") as f:
    f.write(f"Model Accuracy: {accuracy}\n")
    f.write("Classification Report:\n")
    f.write(report)

print(f"Evaluation report saved to {EVALUATION_REPORT_FILE}")
