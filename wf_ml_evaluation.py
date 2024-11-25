import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from wf_ml_training import train_random_forest_model
from wf_ml_prediction import predict_and_save
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score
import joblib

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

# Function to shuffle and split data
def load_split_data(file_path, train_path, test_path, test_size=0.2, shuffle=True, random_state=0):
    data = pd.read_csv(file_path)
    train, test = train_test_split(data, test_size=test_size, shuffle=shuffle, random_state=random_state)
    if len(test) < 30:
        raise ValueError(f"The test set for {file_path} has fewer than 30 samples.")
    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)
    print(f"Data from {file_path} split and saved to {train_path} and {test_path}.")

# Evaluate the random forest model : Function to compute evaluation metrics
def evaluate_model(predictions_path, evaluation_summary_path):
    df_predictions = pd.read_csv(predictions_path)
    y_test = df_predictions['Actual PartyAffiliation']
    y_pred = df_predictions['Predicted_PartyAffiliation']

    accuracy = accuracy_score(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)
   
    os.makedirs(os.path.dirname(evaluation_summary_path), exist_ok=True)
    with open(evaluation_summary_path, 'w') as f:
        f.write("Evaluation Metrics for Random Forest Model\n")
        f.write(f"Model Accuracy: {accuracy}\n\n")
        f.write("Classification Report:\n")
        f.write(class_report)
        f.write("\n")
        f.write("\n")
    print(f"Evaluation metrics saved to {evaluation_summary_path}")

# Train and evaluate KNN models for k =3, 5, 7
def train_and_evaluate_knn(k_values, df1_train_path, df2_train_path, df3_train_path, df1_test_path, df2_test_path, df3_test_path):
    df1_train = pd.read_csv(df1_train_path)
    df2_train = pd.read_csv(df2_train_path)
    df3_train = pd.read_csv(df3_train_path)
    df_train = df2_train.merge(df1_train, on="State", how="left").merge(df3_train, on=["State", "Year"], how="left").dropna()

    df1_test = pd.read_csv(df1_test_path)
    df2_test = pd.read_csv(df2_test_path)
    df3_test = pd.read_csv(df3_test_path)
    df_test = df2_test.merge(df1_test, on="State", how="left").merge(df3_test, on=["State", "Year"], how="left").dropna()

    label_encoders = {
        'PartyAffiliation': joblib.load("models/PartyAffiliation_encoder.pkl"),
        'Ethnicity': joblib.load("models/Ethnicity_encoder.pkl"),
        'Education': joblib.load("models/Education_encoder.pkl")
    }

    for df in [df_train, df_test]:
        df['Ethnicity'] = label_encoders['Ethnicity'].transform(df['Ethnicity'])
        df['Education'] = label_encoders['Education'].transform(df['Education'])
        df['PartyAffiliation'] = label_encoders['PartyAffiliation'].transform(df['PartyAffiliation'])

    features = ['Age', 'Income', 'CandidateVotes', 'TotalVotes', 'TurnoutRate', 'Ethnicity', 'Education']
    target = 'PartyAffiliation'

    X_train = df_train[features]
    y_train = df_train[target]
    X_test = df_test[features]
    y_test = df_test[target]

    results = []
    for k in k_values:
        knn_model = KNeighborsClassifier(n_neighbors=k)
        knn_model.fit(X_train, y_train)
        y_pred = knn_model.predict(X_test)

        y_pred_decoded = label_encoders['PartyAffiliation'].inverse_transform(y_pred)
        y_test_decoded = label_encoders['PartyAffiliation'].inverse_transform(y_test)

        accuracy = accuracy_score(y_test_decoded, y_pred_decoded)
        f1 = f1_score(y_test_decoded, y_pred_decoded, average='weighted')
        results.append((k, accuracy, f1))

        predictions_path_knn = f"evaluation/predictions_knn_k{k}.csv"
        os.makedirs(os.path.dirname(predictions_path_knn), exist_ok=True)
        df_test['Predicted_PartyAffiliation'] = y_pred_decoded
        df_test['Actual PartyAffiliation'] = y_test_decoded
        df_test.to_csv(predictions_path_knn, index=False)
        print(f"KNN predictions saved to {predictions_path_knn}")

    return results

def experiment_with_features(model_path, features, encoder_path):
    model = joblib.load(model_path)
    label_encoder = joblib.load(encoder_path)  # Load the label encoder
    print("Model and Label Encoder loaded for experimentation.")

    # Representative samples from predictions.csv
    base_samples = [
        {
            'State': 'Kentucky',
            'Year': 2010,
            'CandidateVotes': 755706,
            'TotalVotes': 1356096,
            'PartyAffiliation': 'REPUBLICAN',
            'Age': 70.0,
            'Income': 124999.5,
            'Ethnicity': 4,
            'Education': 2,
            'TurnoutRate': 0.445
        },
        {
            'State': 'Arizona',
            'Year': 2000,
            'CandidateVotes': 108926,
            'TotalVotes': 1397076,
            'PartyAffiliation': 'OTHER',
            'Age': 59.5,
            'Income': 62499.5,
            'Ethnicity': 4,
            'Education': 4,
            'TurnoutRate': 0.4637
        },
        {
            'State': 'Florida',
            'Year': 2000,
            'CandidateVotes': 2989487,
            'TotalVotes': 5856731,
            'PartyAffiliation': 'DEMOCRAT',
            'Age': 70.0,
            'Income': 124999.5,
            'Ethnicity': 4,
            'Education': 2,
            'TurnoutRate': 0.5605
        },
        {
            'State': 'Indiana',
            'Year': 2000,
            'CandidateVotes': 33992,
            'TotalVotes': 2145209,
            'PartyAffiliation': 'LIBERTARIAN',
            'Age': 29.5,
            'Income': 87499.5,
            'Ethnicity': 1,
            'Education': 4,
            'TurnoutRate': 0.5102
        }
    ]

    results = []

    for i, base_sample in enumerate(base_samples, start=1):
        print(f"Experimenting with Base Sample {i}: {base_sample}")
        
        # Experiment 1: Vary Candidate Votes
        print("Varying Candidate Votes...")
        for candidate_votes in range(10000, 110000, 10000):
            sample = base_sample.copy()
            sample['CandidateVotes'] = candidate_votes

            # Ensure only features are passed to the model
            feature_sample = {key: sample[key] for key in features}
            prediction_encoded = model.predict(pd.DataFrame([feature_sample]))[0]
            prediction_decoded = label_encoder.inverse_transform([prediction_encoded])[0]
            results.append((candidate_votes, sample['TurnoutRate'], prediction_decoded, f"Sample {i}"))

        # Experiment 2: Vary Turnout Rate
        print("Varying Turnout Rate...")
        for turnout_rate in [x / 100 for x in range(10, 100, 10)]:
            sample = base_sample.copy()
            sample['TurnoutRate'] = turnout_rate

            # Ensure only features are passed to the model
            feature_sample = {key: sample[key] for key in features}
            prediction_encoded = model.predict(pd.DataFrame([feature_sample]))[0]
            prediction_decoded = label_encoder.inverse_transform([prediction_encoded])[0]
            results.append((sample['CandidateVotes'], turnout_rate, prediction_decoded, f"Sample {i}"))

        # Experiment 3: Vary Candidate Votes and Turnout Rate Together (Correlated)
        print("Varying Candidate Votes and Turnout Rate Together (Correlated)...")
        for candidate_votes, turnout_rate in zip(range(10000, 110000, 10000), [x / 100 for x in range(10, 100, 10)]):
            sample = base_sample.copy()
            sample['CandidateVotes'] = candidate_votes
            sample['TurnoutRate'] = turnout_rate

            # Ensure only features are passed to the model
            feature_sample = {key: sample[key] for key in features}
            prediction_encoded = model.predict(pd.DataFrame([feature_sample]))[0]
            prediction_decoded = label_encoder.inverse_transform([prediction_encoded])[0]
            results.append((candidate_votes, turnout_rate, prediction_decoded, f"Sample {i} (Correlated)"))

        # Experiment 4: Vary Candidate Votes and Turnout Rate Together (Inversely Correlated)
        print("Varying Candidate Votes and Turnout Rate Together (Inversely Correlated)...")
        for candidate_votes, turnout_rate in zip(range(10000, 110000, 10000), reversed([x / 100 for x in range(10, 100, 10)])):
            sample = base_sample.copy()
            sample['CandidateVotes'] = candidate_votes
            sample['TurnoutRate'] = turnout_rate

            # Ensure only features are passed to the model
            feature_sample = {key: sample[key] for key in features}
            prediction_encoded = model.predict(pd.DataFrame([feature_sample]))[0]
            prediction_decoded = label_encoder.inverse_transform([prediction_encoded])[0]
            results.append((candidate_votes, turnout_rate, prediction_decoded, f"Sample {i} (Inversely Correlated)"))

    return results

def main():
    print("Starting the ML Workflow....")
    print("Splitting data into training and testing sets...")
    load_split_data(DF1_PATH, DF1_TRAIN, DF1_TEST)
    load_split_data(DF2_PATH, DF2_TRAIN, DF2_TEST)
    load_split_data(DF3_PATH, DF3_TRAIN, DF3_TEST)
    print("Data split successfully.")

    print("Training Random Forest model...")
    train_random_forest_model(DF1_TRAIN, DF2_TRAIN, DF3_TRAIN, model_save_path=MODEL_SAVE_PATH)
    print("Random Forest model trained and saved.")

    print("Generating predictions for the random forest model...")
    predict_and_save(MODEL_SAVE_PATH, DF1_TEST, DF2_TEST, DF3_TEST)
    print("Predictions generated and saved.")

    print("Evaluating the model random forest model...")
    evaluate_model(PREDICTIONS_PATH, EVALUATION_SUMMARY_PATH)
    print("Model evaluation completed.")

    print("Training and evaluating KNN models...")
    k_values = [3, 5, 7]
    knn_results = train_and_evaluate_knn(k_values, DF1_TRAIN, DF2_TRAIN, DF3_TRAIN, DF1_TEST, DF2_TEST, DF3_TEST)
    for k, acc, f1 in knn_results:
        with open(EVALUATION_SUMMARY_PATH, 'a') as f:
            f.write(f"KNN (k={k}) -> Accuracy: {acc:.4f}, F1 Score: {f1:.4f}\n")
            
    print("Generating visualizations...")        
            
    # Visual 1 : Model Performance Comparison (Accuracy and F1-Score) for all models
    models = ['Random Forest', 'KNN (k=3)', 'KNN (k=5)', 'KNN (k=7)']
    accuracy = [0.7645, 0.6435, 0.6448, 0.6564]
    f1_score = [0.73, 0.6270, 0.6303, 0.6368]
    performance_df = pd.DataFrame({'Model': models, 'Accuracy': accuracy, 'F1-Score': f1_score})
    performance_df.set_index('Model').plot(kind='bar', figsize=(10, 6), rot=0)
    plt.title('Model Performance Comparison (Accuracy and F1-Score)')
    plt.ylabel('Score')
    plt.legend(loc='lower right')
    plt.savefig('visuals/model_comparison_f1vsAccuracy.png')
    
    # Visual 2 : Feature Importance (Random Forest Classifier)
    features = ['Turnout Rate', 'Ethnicity', 'Education', 'Candidate Votes', 'Total Votes', 'Age', 'Income']
    importance = [0.127159699394538, 0.007856609425618208, 0.016764008059805907, 0.6529026154425202, 0.1689909065781081, 0.014496068577102532, 0.011830092522307132]
    plt.figure(figsize=(10, 6))
    plt.barh(features, importance, color='skyblue')
    plt.xlabel('Feature Importance')
    plt.title('Feature Importance (Random Forest Classifier)')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('visuals/feature_importance_rf.png')

    # Visual 3 : Confusion Matrix (Random Forest Classifier)
    cm_rf = np.array([[ 80,  28,  24,   0],
                      [  1, 388,   0,   9],
                      [ 44,   5, 120,   0],
                      [  0,  72,   0,   6]])
    classes = ['DEMOCRAT', 'LIBERTARIAN', 'OTHER', 'REPUBLICAN']

    plt.figure(figsize=(8, 8))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm_rf, display_labels=classes)
    disp.plot(cmap='Blues', values_format='d', ax=plt.gca())
    plt.title('Confusion Matrix (Random Forest Classifier)')
    plt.tight_layout()
    plt.savefig('visuals/confusion_matrix_rf.png')

    print("Visualizations generated successfully and saved to visuals folder")
    
    model_path = 'models/random_forest_model.pkl'
    encoder_path = 'models/PartyAffiliation_encoder.pkl'
    features = ['Age', 'Income', 'CandidateVotes', 'TotalVotes', 'TurnoutRate', 'Ethnicity', 'Education']
    results = experiment_with_features(model_path, features, encoder_path)
    for r in results:
        print(f"Candidate Votes: {r[0]}, Turnout Rate: {r[1]}, Predicted Party Affiliation: {r[2]}, Sample: {r[3]}")
        
if __name__ == "__main__":
    main()

   


    
    

