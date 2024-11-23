import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.class_weight import compute_class_weight
from sklearn.preprocessing import LabelEncoder

# I was eariler planning to use XgBoost with hyperparameter tuning
# However, I am using RandomForestClassifier for simplicity

# from sklearn.model_selection import GridSearchCV, train_test_split
# import xgboost as xgb

import joblib

def train_random_forest_model(df1_path, df2_path, df3_path, model_save_path='models/random_forest_model.pkl'):
    
    df1_train = pd.read_csv(df1_path)
    df2_train = pd.read_csv(df2_path)
    df3_train = pd.read_csv(df3_path)

    df_combined = df2_train.merge(df1_train, on="State", how="left").merge(df3_train, on=["State", "Year"], how="left")
    df_combined = df_combined.dropna()

    label_encoders = {
        'PartyAffiliation': LabelEncoder(),
        'Ethnicity': LabelEncoder(),
        'Education': LabelEncoder()
    }
    df_combined['PartyAffiliation'] = label_encoders['PartyAffiliation'].fit_transform(df_combined['PartyAffiliation'])
    df_combined['Ethnicity'] = label_encoders['Ethnicity'].fit_transform(df_combined['Ethnicity'])
    df_combined['Education'] = label_encoders['Education'].fit_transform(df_combined['Education'])

    os.makedirs("models", exist_ok=True)
    for col, encoder in label_encoders.items():
        joblib.dump(encoder, f"models/{col}_encoder.pkl")

    # Define features and target for model training
    features = ['Age', 'Income', 'CandidateVotes', 'TotalVotes', 'TurnoutRate', 'Ethnicity', 'Education']
    target = 'PartyAffiliation'

    X = df_combined[features]
    y = df_combined[target]
    
    unique_classes = label_encoders['PartyAffiliation'].classes_
    class_weights = compute_class_weight('balanced', classes=np.array(range(len(unique_classes))), y=y)

    # Convert weights to dictionary
    class_weight_dict = {i: class_weights[i] for i in range(len(unique_classes))}

    # Train the Random Forest Classifier
    rf_classifier = RandomForestClassifier(random_state=42, class_weight=class_weight_dict)
    rf_classifier.fit(X, y)

    # Save the trained model to the specified path
    joblib.dump(rf_classifier, model_save_path)
    print(f"Random Forest Model saved to {model_save_path}")

