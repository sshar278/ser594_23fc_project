import os
import pandas as pd
from sklearn.model_selection import train_test_split
from wf_ml_training import train_random_forest_model
from wf_ml_prediction import predict_and_save
from sklearn.metrics import accuracy_score, classification_report

DATA_PROCESSED_PATH = 'data_processed'
DF1_PATH = os.path.join(DATA_PROCESSED_PATH, 'df1_processed.csv')
DF2_PATH = os.path.join(DATA_PROCESSED_PATH, 'df2_processed.csv')
DF3_PATH = os.path.join(DATA_PROCESSED_PATH, 'df3_processed.csv')

DF1_TRAIN = os.path.join(DATA_PROCESSED_PATH, 'df1_train.csv')
DF1_TEST = os.path.join(DATA_PROCESSED_PATH, 'df1_test.csv')
DF2_TRAIN = os.path.join(DATA_PROCESSED_PATH, 'df2_train.csv')
DF2_TEST = os.path.join(DATA_PROCESSED_PATH, 'df2_test.csv')
DF3_TRAIN = os.path.join(DATA_PROCESSED_PATH, 'df3_train.csv')
DF3_TEST = os.path.join(DATA_PROCESSED_PATH, 'df3_test.csv')

MODEL_SAVE_PATH = 'models/random_forest_model.pkl'
PREDICTIONS_PATH = 'evaluation/predictions.csv'
EVALUATION_SUMMARY_PATH = 'evaluation/summary.txt'

# Function to shuffle and split data without scaling
def load_split_data(file_path, train_path, test_path, test_size=0.2, shuffle=True, random_state=0):
    
    data = pd.read_csv(file_path)
    train, test = train_test_split(data, test_size=test_size, shuffle=shuffle, random_state=random_state)
    
    if len(test) < 30:
        raise ValueError(f"The test set for {file_path} has fewer than 30 samples.")
    
    # Save training and testing splits
    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)
    print(f"Data from {file_path} split and saved to {train_path} and {test_path}.")
    
    
def evaluate_model(predictions_path, evaluation_summary_path):
    """
    Reads the predictions file and evaluates the model.
    :param predictions_path: Path to the predictions CSV file.
    :param evaluation_summary_path: Path to save the evaluation summary file.
    """
    # Load predictions
    df_predictions = pd.read_csv(predictions_path)

    # Extract actual and predicted labels
    y_test = df_predictions['Actual PartyAffiliation']
    y_pred = df_predictions['Predicted_PartyAffiliation']

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    # Save evaluation metrics to file
    os.makedirs(os.path.dirname(evaluation_summary_path), exist_ok=True)
    with open(evaluation_summary_path, 'w') as f:
        f.write(f"Model Accuracy: {accuracy}\n\n")
        f.write("Classification Report:\n")
        f.write(class_report)
    print(f"Evaluation metrics saved to {evaluation_summary_path}")    
    
    
    
def main():
    
    print("Starting the ML Workflow....")
    
    # STEP 1: Split the data into training and testing sets.
    print("Splitting data into training and testing sets...")
    # Split and shuffle the data
    load_split_data(DF1_PATH, DF1_TRAIN, DF1_TEST)
    load_split_data(DF2_PATH, DF2_TRAIN, DF2_TEST)
    load_split_data(DF3_PATH, DF3_TRAIN, DF3_TEST)
    print("Data split successfully.")
    
    
    # STEP 2: Train the Random Forest model
    print("Training Random Forest model...")
    train_random_forest_model(DF1_TRAIN, DF2_TRAIN, DF3_TRAIN, model_save_path=MODEL_SAVE_PATH)
    print("Random Forest model trained and saved.")
    
    # STEP 3: Generate predictions and save to a file
    print("Generating predictions...")
    predict_and_save(MODEL_SAVE_PATH, DF1_TEST, DF2_TEST, DF3_TEST)
    print("Predictions generated and saved.")
    
    # STEP 4: Evaluate the model using the predictions file
    print("Evaluating the model...")
    evaluate_model(PREDICTIONS_PATH, EVALUATION_SUMMARY_PATH)
    print("Model evaluation completed.")



if __name__ == "__main__":
    main()
    
    

