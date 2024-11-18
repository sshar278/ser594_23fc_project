import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import GridSearchCV, train_test_split
# import xgboost as xgb
import joblib

def train_random_forest_model(df1_path, df2_path, df3_path, model_save_path='models/random_forest_model.pkl'):
    # Load datasets
    df1_train = pd.read_csv(df1_path)
    df2_train = pd.read_csv(df2_path)
    df3_train = pd.read_csv(df3_path)

    # Merge datasets on 'State' and 'Year' where applicable
    df_combined = df2_train.merge(df1_train, on="State", how="left").merge(df3_train, on=["State", "Year"], how="left")
    df_combined = df_combined.dropna()

    # Encoding categorical features
    label_encoders = {
        'PartyAffiliation': LabelEncoder(),
        'Ethnicity': LabelEncoder(),
        'Education': LabelEncoder()
    }
    df_combined['PartyAffiliation'] = label_encoders['PartyAffiliation'].fit_transform(df_combined['PartyAffiliation'])
    df_combined['Ethnicity'] = label_encoders['Ethnicity'].fit_transform(df_combined['Ethnicity'])
    df_combined['Education'] = label_encoders['Education'].fit_transform(df_combined['Education'])

    # Save the encoders for consistency during prediction
    os.makedirs("models", exist_ok=True)
    for col, encoder in label_encoders.items():
        joblib.dump(encoder, f"models/{col}_encoder.pkl")

    # Define features and target for model training
    features = ['Age', 'Income', 'CandidateVotes', 'TotalVotes', 'TurnoutRate', 'Ethnicity', 'Education']
    target = 'PartyAffiliation'

    X = df_combined[features]
    y = df_combined[target]

    # Train the Random Forest Classifier
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(X, y)

    # Save the trained model to the specified path
    joblib.dump(rf_classifier, model_save_path)
    print(f"Random Forest Model saved to {model_save_path}")


# def train_random_forest_with_tuning(df1_path, df2_path, df3_path, model_save_path='models/random_forest_model.pkl'):
#     # Load datasets
#     df1_train = pd.read_csv(df1_path)
#     df2_train = pd.read_csv(df2_path)
#     df3_train = pd.read_csv(df3_path)

#     # Merge datasets on 'State' and 'Year' where applicable
#     df_combined = df2_train.merge(df1_train, on="State", how="left").merge(df3_train, on=["State", "Year"], how="left")
#     df_combined = df_combined.dropna()

#     # Encoding categorical features
#     label_encoders = {
#         'PartyAffiliation': LabelEncoder(),
#         'Ethnicity': LabelEncoder(),
#         'Education': LabelEncoder()
#     }

#     df_combined['PartyAffiliation'] = label_encoders['PartyAffiliation'].fit_transform(df_combined['PartyAffiliation'])
#     df_combined['Ethnicity'] = label_encoders['Ethnicity'].fit_transform(df_combined['Ethnicity'])
#     df_combined['Education'] = label_encoders['Education'].fit_transform(df_combined['Education'])

#     # Save the encoders
#     os.makedirs("models", exist_ok=True)
#     for col, encoder in label_encoders.items():
#         joblib.dump(encoder, f"models/{col}_encoder.pkl")

#     # Define features and target
#     features = ['Age', 'Income', 'CandidateVotes', 'TotalVotes', 'TurnoutRate', 'Ethnicity', 'Education']
#     target = 'PartyAffiliation'

#     X = df_combined[features]
#     y = df_combined[target]

#     # Random Forest with Grid Search for Hyperparameter Tuning
#     rf_classifier = RandomForestClassifier(random_state=42)
#     param_grid = {
#         'n_estimators': [100, 200, 300],
#         'max_depth': [10, 20, 30],
#         'min_samples_split': [2, 5, 10],
#         'min_samples_leaf': [1, 2, 4]
#     }

#     grid_search = GridSearchCV(estimator=rf_classifier, param_grid=param_grid, cv=5, n_jobs=-1, scoring='accuracy')
#     grid_search.fit(X, y)

#     best_rf = grid_search.best_estimator_
#     joblib.dump(best_rf, model_save_path)
#     print(f"Random Forest Model saved to {model_save_path} with best parameters: {grid_search.best_params_}")

#     return best_rf, grid_search.best_score_

# def train_xgboost_model(df1_path, df2_path, df3_path, model_save_path='models/xgboost_model.pkl'):
#     # Load datasets
#     df1_train = pd.read_csv(df1_path)
#     df2_train = pd.read_csv(df2_path)
#     df3_train = pd.read_csv(df3_path)

#     # Merge datasets on 'State' and 'Year' where applicable
#     df_combined = df2_train.merge(df1_train, on="State", how="left").merge(df3_train, on=["State", "Year"], how="left")
#     df_combined = df_combined.dropna()

#     # Encoding categorical features
#     label_encoders = {
#         'PartyAffiliation': LabelEncoder(),
#         'Ethnicity': LabelEncoder(),
#         'Education': LabelEncoder()
#     }

#     df_combined['PartyAffiliation'] = label_encoders['PartyAffiliation'].fit_transform(df_combined['PartyAffiliation'])
#     df_combined['Ethnicity'] = label_encoders['Ethnicity'].fit_transform(df_combined['Ethnicity'])
#     df_combined['Education'] = label_encoders['Education'].fit_transform(df_combined['Education'])

#     # Save the encoders
#     for col, encoder in label_encoders.items():
#         joblib.dump(encoder, f"models/{col}_encoder.pkl")

#     # Define features and target
#     features = ['Age', 'Income', 'CandidateVotes', 'TotalVotes', 'TurnoutRate', 'Ethnicity', 'Education']
#     target = 'PartyAffiliation'

#     X = df_combined[features]
#     y = df_combined[target]

#     # Train an XGBoost Classifier
#     xgb_classifier = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
#     xgb_classifier.fit(X, y)

#     # Save the model
#     joblib.dump(xgb_classifier, model_save_path)
#     print(f"XGBoost Model saved to {model_save_path}")

#     return xgb_classifier

# if __name__ == "__main__":
#     # Paths to processed data files
#     DATA_PROCESSED_PATH = 'data_processed'
#     df1_path = os.path.join(DATA_PROCESSED_PATH, 'df1_train.csv')
#     df2_path = os.path.join(DATA_PROCESSED_PATH, 'df2_train.csv')
#     df3_path = os.path.join(DATA_PROCESSED_PATH, 'df3_train.csv')

#     # Train and save Random Forest model
#     MODEL_SAVE_PATH_RF = 'models/random_forest_model.pkl'
#     print("Starting Random Forest Model Training...")
#     _, best_rf_score = train_random_forest_with_tuning(df1_path, df2_path, df3_path, model_save_path=MODEL_SAVE_PATH_RF)
#     print(f"Random Forest Best Cross-Validation Accuracy: {best_rf_score}")

#     # Train and save XGBoost model
#     MODEL_SAVE_PATH_XGB = 'models/xgboost_model.pkl'
#     print("Starting XGBoost Model Training...")
#     xgb_model = train_xgboost_model(df1_path, df2_path, df3_path, model_save_path=MODEL_SAVE_PATH_XGB)
