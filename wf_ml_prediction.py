# wf_ml_prediction.py
"""
This script loads the saved model and uses it to make predictions on the test set.
Steps:
1. Load the trained model from the 'models' folder.
2. Load the test data from the 'models' folder.
3. Make predictions using the trained model.
4. Save the prediction results to a CSV file.
"""

import os
import pandas as pd
import joblib

# Paths
MODELS_PATH = "models"
MODEL_FILE = os.path.join(MODELS_PATH, "election_rf_model.pkl")
TEST_DATA_FILE = os.path.join(MODELS_PATH, "test_data.csv")

# Load the trained model
model = joblib.load(MODEL_FILE)

# Load the test data
test_data = pd.read_csv(TEST_DATA_FILE)
X_test = test_data.drop(columns=['target'])  # Replace 'target' with the actual target column name
y_test = test_data['target']

# Make predictions
predictions = model.predict(X_test)

# Output predictions
results = pd.DataFrame({"Actual": y_test, "Predicted": predictions})
results.to_csv(os.path.join(MODELS_PATH, "predictions.csv"), index=False)

print("Predictions saved to models/predictions.csv")