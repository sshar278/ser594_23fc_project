import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('merged_data.db')
df1_selected = pd.read_sql_query("SELECT * FROM table_df1", conn)
df2_selected = pd.read_sql_query("SELECT * FROM table_df2", conn)
df3_selected = pd.read_sql_query("SELECT * FROM table_df3", conn)

# Merge df1_selected and df3_selected on 'State' (merging Age/Income from df1 and TurnoutRate from df3)
merged_df = pd.merge(df1_selected[['Age', 'Income','Education','State']],df3_selected[['TurnoutRate', 'State']], on='State')

# Convert State to a numeric value for plotting
merged_df['State_numeric'] = pd.factorize(merged_df['State'])[0]

# 3. Compute Summary Statistics
# quantitative factors : Age, Income, TurnoutRate
# qualitative : Ethnicity, Education
quantitative_stats = {
    "Age": {
        "min": merged_df["Age"].min(),
        "max": merged_df["Age"].max(),
        "median": merged_df["Age"].median()
    },
    "Income": {
        "min": merged_df["Income"].min(),
        "max": merged_df["Income"].max(),
        "median": merged_df["Income"].median()
    },
    "TurnoutRate": {
        "min": merged_df["TurnoutRate"].min(),
        "max": merged_df["TurnoutRate"].max(),
        "median": merged_df["TurnoutRate"].median()
    }
}

qualitative_stats = {}

ethnicity_counts = df1_selected["Ethnicity"].value_counts()
ethnicity_most_frequent = ethnicity_counts[ethnicity_counts == ethnicity_counts.max()]
ethnicity_least_frequent = ethnicity_counts[ethnicity_counts == ethnicity_counts.min()]
qualitative_stats["Ethnicity"] = {
    "number_of_categories": len(ethnicity_counts),
    "most_frequent_category": ethnicity_most_frequent.to_dict(),
    "least_frequent_category": ethnicity_least_frequent.to_dict()
}

education_counts = df1_selected["Education"].value_counts()
education_most_frequent = education_counts[education_counts == education_counts.max()]
education_least_frequent = education_counts[education_counts == education_counts.min()]
qualitative_stats["Education"] = {
    "number_of_categories": len(education_counts),
    "most_frequent_category": education_most_frequent.to_dict(),
    "least_frequent_category": education_least_frequent.to_dict()
}

with open('ser594_23fc_project\data_processed\summary.txt', 'w') as f:
    f.write("Quantitative Summary Statistics:\n")
    for feature, stats in quantitative_stats.items():
        f.write(f"{feature}:\n")
        f.write(f"  Min: {stats['min']}\n")
        f.write(f"  Max: {stats['max']}\n")
        f.write(f"  Median: {stats['median']}\n")
        f.write("\n")

    f.write("Qualitative Summary Statistics:\n")
    for feature, stats in qualitative_stats.items():
        f.write(f"{feature}:\n")
        f.write(f"  Number of categories: {stats['number_of_categories']}\n")
        f.write(f"  Most frequent category: {stats['most_frequent_category']}\n")
        f.write(f"  Least frequent category: {stats['least_frequent_category']}\n")
        f.write("\n")

print("Summary statistics saved to summary.txt")  

#4. Compute pair-wise correlation matrix
correlation_matrix = merged_df[['Age', 'Income', 'TurnoutRate']].corr()
with open('ser594_23fc_project\data_processed\correlations.txt', 'w') as f:
    f.write(correlation_matrix.to_string())

print("Correlation matrix saved to correlations.txt")

#5. Plots of distributions
output_dir = 'ser594_23fc_project/visuals'
# Adding noise to avoid overlapping points
def add_noise(series, noise_level=0.04):
    return series + np.random.normal(0, noise_level, len(series))
quantitative_features = ['Age', 'Income', 'TurnoutRate']

# Adding a color map based on the State column
unique_states = merged_df['State'].unique()
state_color_map = {state: i for i, state in enumerate(unique_states)}

for i in range(len(quantitative_features)):
    for j in range(i + 1, len(quantitative_features)):
        feature_x = quantitative_features[i]
        feature_y = quantitative_features[j]
        
        plt.figure()
        
        x_with_noise = add_noise(merged_df[feature_x])
        y_with_noise = add_noise(merged_df[feature_y])
        
        plt.scatter(x_with_noise, y_with_noise, c=merged_df['State'].map(state_color_map), alpha=0.5, cmap='tab20')
        plt.title(f'{feature_x} vs {feature_y}')
        plt.xlabel(feature_x)
        plt.ylabel(feature_y)
        plt.colorbar(label='State') 
        plt.savefig(f'ser594_23fc_project/visuals/{feature_x}_vs_{feature_y}_colored_scatter.png')
        plt.close()
        
# Scatter Plot: Age vs Income with State as Z-axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(merged_df['Age'], merged_df['Income'], merged_df['State_numeric'], c=merged_df['Income'], cmap='viridis', s=50)
ax.set_xlabel('Age')
ax.set_ylabel('Income')
ax.set_zlabel('State (encoded)')
ax.set_title('3D Scatter: Age vs Income by State')
plt.savefig('ser594_23fc_project/visuals/3d_age_income_state.png')

# Scatter Plot: Age vs TurnoutRate with State as Z-axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(merged_df['Age'], merged_df['TurnoutRate'], merged_df['State_numeric'], c=merged_df['TurnoutRate'], cmap='plasma', s=50)
ax.set_xlabel('Age')
ax.set_ylabel('Turnout Rate')
ax.set_zlabel('State (encoded)')
ax.set_title('3D Scatter: Age vs Turnout Rate by State')
plt.savefig('ser594_23fc_project/visuals/3d_age_turnout_rate.png')

# Histogram for State Distribution
plt.figure(figsize=(10, 6))
merged_df['State'].value_counts().plot(kind='bar', color='c')
plt.title('State Distribution')
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout(pad=2)
plt.savefig('ser594_23fc_project/visuals/histogram_state.png')

# Histogram for Ethnicity Distribution
plt.figure(figsize=(10, 6))
df1_selected['Ethnicity'].value_counts().plot(kind='bar', color='orange')
plt.title('Ethnicity Distribution')
plt.xlabel('Ethnicity')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout(pad=2)
plt.savefig('ser594_23fc_project/visuals/histogram_ethnicity.png')

print("Scatter plots and histograms saved in the 'visuals' folder.")

