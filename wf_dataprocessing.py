"""All the data munging tasks (cleaning, transforming, feature engineering etc.) , saves the 
processed data in the data_processed folder
"""

import pandas as pd
import sqlite3
import re
import numpy as np

# Loading the datasets
df1 = pd.read_csv('ser594_23fc_project\\data_original\\US Elections Poll 2020 - Qriously.csv')
df2 = pd.read_csv('ser594_23fc_project\\data_original\\1976-2020-senate.csv')
df3 = pd.read_csv('ser594_23fc_project\\data_original\\Turnout_1980_2022_v1.1.csv')

# Rename columns to match for merging on the 'State' field
df1.rename(columns={'How old are you?': 'Age'}, inplace=True)
df1.rename(columns={'What was your yearly household income at the end of last year (before tax)?': 'Income'}, inplace=True)
df1.rename(columns={'race_ethnicity_grouped': 'Ethnicity'}, inplace=True)
df1.rename(columns={'What is the highest degree or level of school you have _completed_ ?': 'Education'}, inplace=True)
df2.rename(columns={'state': 'State'}, inplace=True)
df2.rename(columns={'year': 'Year'}, inplace=True)
df2.rename(columns={'totalvotes': 'TotalVotes'}, inplace=True)
df2.rename(columns={'candidatevotes': 'CandidateVotes'}, inplace=True)
df2.rename(columns={'party_simplified': 'PartyAffiliation'}, inplace=True)
df3.rename(columns={'STATE': 'State'}, inplace=True)
df3.rename(columns={'YEAR': 'Year'}, inplace=True)
df3.rename(columns={'VEP_TURNOUT_RATE': 'TurnoutRate'}, inplace=True)


state_abbreviation_map = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# Function to clean and format state names in order to properly merge the datasets
def clean_state(state_name):
    if isinstance(state_name, str):
        cleaned = re.sub(r'[^A-Za-z\s]', '', state_name)

        if cleaned in state_abbreviation_map:
            cleaned = state_abbreviation_map[cleaned]

        cleaned = cleaned.title().strip()

        return cleaned
    return state_name

# Functions for Age, Income, and Turnout Rate conversion
def convert_age_to_midpoint(age_range):
    if isinstance(age_range, str) and '-' in age_range:
        parts = age_range.split('-')
        return (int(parts[0]) + int(parts[1])) / 2
    elif isinstance(age_range, str) and '+' in age_range:
        return int(age_range.replace('+', '')) + 5
    return np.nan

def convert_income_to_midpoint(income_range):
    if isinstance(income_range, str) and 'to' in income_range:
        income_range = income_range.replace('$', '').replace(',', '')
        parts = income_range.split(' to ')
        return (int(parts[0]) + int(parts[1])) / 2
    elif isinstance(income_range, str) and 'or more' in income_range:
        return int(income_range.replace('$', '').replace(',', '').replace(' or more', '')) + 25000
    return np.nan

def convert_percentage_to_float(percentage):
    if isinstance(percentage, str):
        return float(percentage.replace('%', '')) / 100
    return np.nan

# Apply the conversion to the Age, Income, and TurnoutRate columns
df1['Age'] = df1['Age'].apply(convert_age_to_midpoint)
df1['Income'] = df1['Income'].apply(convert_income_to_midpoint)
df3['TurnoutRate'] = df3['TurnoutRate'].apply(convert_percentage_to_float)


# Apply the cleaning function to the State column for all three datasets
df1['State'] = df1['State'].apply(clean_state)
df2['State'] = df2['State'].apply(clean_state)
df3['State'] = df3['State'].apply(clean_state)

# Select only the specified columns for each dataframe
df1_selected = df1[['Age', 'State', 'Income', 'Ethnicity', 'Education']]
df2_selected = df2[['State', 'Year', 'CandidateVotes', 'TotalVotes', 'PartyAffiliation']]
df3_selected = df3[['State', 'Year', 'TurnoutRate']]

# Drop any rows with missing values and remove duplicates
df1_selected.dropna(subset=['Income'], inplace=True)
df3_selected.dropna(subset=['TurnoutRate'], inplace=True)
df1_selected.drop_duplicates(inplace=True)
df2_selected.drop_duplicates(inplace=True)
df3_selected.drop_duplicates(inplace=True)

# Storing the series of processed data in the data_processed folder
# In order to verify this, you can first delete the data_processed folder and then run this script
df1_selected.to_csv('ser594_23fc_project/data_processed/df1_processed.csv', index=False)
df2_selected.to_csv('ser594_23fc_project/data_processed/df2_processed.csv', index=False)
df3_selected.to_csv('ser594_23fc_project/data_processed/df3_processed.csv', index=False)

# Connect to the SQLite database (or create it if it doesn't exist)
# The merged_data.db file is generateed dynamically everytime when you run this script
conn = sqlite3.connect('ser594_23fc_project/merged_data.db')

# Save each dataframe into a separate table
df1_selected.to_sql('table_df1', conn, if_exists='replace', index=False)
df2_selected.to_sql('table_df2', conn, if_exists='replace', index=False)
df3_selected.to_sql('table_df3', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

print("Data has been cleaned and saved into three separate tables: 'table_df1', 'table_df2', and 'table_df3' in 'merged_data.db' as well as eparate CSV files in the 'data_processed' folder.")




