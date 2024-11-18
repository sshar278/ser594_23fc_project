import os
import pandas as pd
import joblib


def predict_and_save(model_path, df1_test_path, df2_test_path, df3_test_path, input_data=None):
    """
    Perform predictions on test data, evaluate model, and optionally predict for a single input.
    :param model_path: Path to the saved model.
    :param df1_test_path: Path to df1 test file.
    :param df2_test_path: Path to df2 test file.
    :param df3_test_path: Path to df3 test file.
    :param input_data: Optional dictionary containing a single input to predict.
    """
    # Load the saved model
    model = joblib.load(model_path)
    print(f"Model loaded from {model_path}")

    # Load test datasets
    df1_test = pd.read_csv(df1_test_path)
    df2_test = pd.read_csv(df2_test_path)
    df3_test = pd.read_csv(df3_test_path)

    # Merge test datasets on 'State' and 'Year' where applicable
    df_combined_test = df2_test.merge(df1_test, on="State", how="left").merge(df3_test, on=["State", "Year"], how="left")
    df_combined_test = df_combined_test.dropna()

    # Load encoders and apply encoding to categorical features
    label_encoders = {
        'PartyAffiliation': joblib.load("models/PartyAffiliation_encoder.pkl"),
        'Ethnicity': joblib.load("models/Ethnicity_encoder.pkl"),
        'Education': joblib.load("models/Education_encoder.pkl")
    }
    df_combined_test['PartyAffiliation'] = label_encoders['PartyAffiliation'].transform(df_combined_test['PartyAffiliation'])
    df_combined_test['Ethnicity'] = label_encoders['Ethnicity'].transform(df_combined_test['Ethnicity'])
    df_combined_test['Education'] = label_encoders['Education'].transform(df_combined_test['Education'])

    # Define features and target for testing
    features = ['Age', 'Income', 'CandidateVotes', 'TotalVotes', 'TurnoutRate', 'Ethnicity', 'Education']
    target = 'PartyAffiliation'

    X_test = df_combined_test[features]
    y_test = df_combined_test[target]

    # Make predictions on the test data
    y_pred = model.predict(X_test)
    
    y_pred_decoded = label_encoders['PartyAffiliation'].inverse_transform(y_pred)
    y_test_decoded = label_encoders['PartyAffiliation'].inverse_transform(y_test)
    
    # Save predictions to a file
    predictions_path = os.path.join('evaluation', 'predictions.csv')
    os.makedirs(os.path.dirname(predictions_path), exist_ok=True)
    df_combined_test['Predicted_PartyAffiliation'] = y_pred_decoded
    df_combined_test['Actual PartyAffiliation'] = y_test_decoded
    df_combined_test.to_csv(predictions_path, index=False)
    print(f"Predictions saved to {predictions_path}")
    
    if input_data:
        input_df = pd.DataFrame([input_data])
        # Encode the input using the same encoders
        input_df['Ethnicity'] = label_encoders['Ethnicity'].transform([input_data['Ethnicity']])
        input_df['Education'] = label_encoders['Education'].transform([input_data['Education']])
        input_features = input_df[features]
        input_prediction = model.predict(input_features)
        input_prediction_label = label_encoders['PartyAffiliation'].inverse_transform(input_prediction)
        print(f"Prediction for input: {input_data} => {input_prediction_label[0]}")
        return input_prediction_label[0]


    
