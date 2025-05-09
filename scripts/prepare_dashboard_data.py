import pandas as pd
import numpy as np
import os

# Ensure output directory exists
os.makedirs('../data/processed/dashboard_data', exist_ok=True)

# Load the analyzed dataset
df = pd.read_csv('../data/processed/mental_health_tech_analyzed.csv')

# Create an ID column if it doesn't exist
if 'id' not in df.columns:
    df['id'] = range(1, len(df) + 1)

# 1. Create yearly summary for trend analysis
yearly_summary = df.groupby('year').agg({
    'mental_health_benefits_binary': 'mean',
    'mental_health_benefits_awareness_binary': 'mean',
    'employer_mental_health_discussion_binary': 'mean',
    'employer_mental_health_learning_resources_binary': 'mean',
    'mental_health_treatment_anonymity_binary': 'mean',
    'mental_health_discussion_comfort_coworkers_binary': 'mean',
    'mental_health_discussion_comfort_supervisor_binary': 'mean'
}).reset_index()

# Rename columns for clarity
yearly_summary.columns = ['Year', 'Benefits_Offered', 'Benefits_Awareness', 
                         'Employer_Discussion', 'Learning_Resources', 
                         'Anonymity', 'Comfort_Coworkers', 'Comfort_Supervisor']

# Convert to percentages
for col in yearly_summary.columns:
    if col != 'Year':
        yearly_summary[col] = yearly_summary[col] * 100

# Save for dashboard
yearly_summary.to_csv('../data/processed/dashboard_data/yearly_trends.csv', index=False)

# 2. Company size analysis
size_summary = df.groupby('number_of_employees').agg({
    'mental_health_benefits_binary': 'mean',
    'employer_mental_health_discussion_binary': 'mean',
    'mental_health_discussion_comfort_supervisor_binary': 'mean',
    'id': 'count'  # Count of responses
}).reset_index()

size_summary.columns = ['Company_Size', 'Benefits_Offered', 'Employer_Discussion', 
                        'Comfort_Supervisor', 'Response_Count']

# Convert to percentages
for col in ['Benefits_Offered', 'Employer_Discussion', 'Comfort_Supervisor']:
    size_summary[col] = size_summary[col] * 100

# Save for dashboard
size_summary.to_csv('../data/processed/dashboard_data/company_size_analysis.csv', index=False)

# 3. Tech vs Non-Tech comparison
tech_summary = df.groupby('tech_company').agg({
    'mental_health_benefits_binary': 'mean',
    'mental_health_benefits_awareness_binary': 'mean',
    'employer_mental_health_discussion_binary': 'mean',
    'employer_mental_health_learning_resources_binary': 'mean',
    'mental_health_treatment_anonymity_binary': 'mean',
    'mental_health_discussion_comfort_coworkers_binary': 'mean',
    'mental_health_discussion_comfort_supervisor_binary': 'mean',
    'id': 'count'  # Count of responses
}).reset_index()

tech_summary.columns = ['Tech_Company', 'Benefits_Offered', 'Benefits_Awareness', 
                       'Employer_Discussion', 'Learning_Resources', 
                       'Anonymity', 'Comfort_Coworkers', 'Comfort_Supervisor', 
                       'Response_Count']

# Convert to percentages
for col in tech_summary.columns:
    if col not in ['Tech_Company', 'Response_Count']:
        tech_summary[col] = tech_summary[col] * 100

# Save for dashboard
tech_summary.to_csv('../data/processed/dashboard_data/tech_vs_nontech.csv', index=False)

# 4. Self-employed vs. Employed analysis
employment_summary = df.groupby('self_employed').agg({
    'mental_health_benefits_binary': 'mean',
    'mental_health_discussion_comfort_coworkers_binary': 'mean',
    'mental_health_discussion_comfort_supervisor_binary': 'mean',
    'id': 'count'  # Count of responses
}).reset_index()

employment_summary.columns = ['Self_Employed', 'Benefits_Offered', 
                             'Comfort_Coworkers', 'Comfort_Supervisor', 
                             'Response_Count']

# Convert to percentages
for col in ['Benefits_Offered', 'Comfort_Coworkers', 'Comfort_Supervisor']:
    employment_summary[col] = employment_summary[col] * 100

# Save for dashboard
employment_summary.to_csv('../data/processed/dashboard_data/employment_type.csv', index=False)

# 5. Correlation matrix for dashboard
binary_columns = [col for col in df.columns if col.endswith('_binary')]
correlation_df = df[binary_columns].corr().reset_index()
correlation_df.columns = ['Variable'] + binary_columns

# Reshape for visualization in dashboard
correlation_long = pd.melt(correlation_df, id_vars=['Variable'], 
                           value_vars=binary_columns,
                           var_name='Related_Variable', value_name='Correlation')

# Save for dashboard
correlation_long.to_csv('../data/processed/dashboard_data/correlation_matrix.csv', index=False)

# 6. Prepare data for PowerBI/Tableau
# Create a consolidated file with all important metrics
powerbi_data = df.copy()

# Rename columns for clarity in PowerBI
column_mapping = {
    'year': 'Year',
    'self_employed': 'Self_Employed',
    'number_of_employees': 'Company_Size',
    'tech_company': 'Tech_Company',
    'mental_health_benefits': 'Benefits_Offered',
    'mental_health_benefits_awareness': 'Benefits_Awareness',
    'employer_mental_health_discussion': 'Employer_Discussion',
    'employer_mental_health_learning_resources': 'Learning_Resources',
    'mental_health_treatment_anonymity': 'Treatment_Anonymity',
    'mental_health_leave_accessibility': 'Leave_Accessibility',
    'mental_health_discussion_comfort_coworkers': 'Comfort_Coworkers',
    'mental_health_discussion_comfort_supervisor': 'Comfort_Supervisor'
}

# Rename columns
powerbi_data = powerbi_data.rename(columns=column_mapping)

# Select only the most relevant columns for the dashboard
powerbi_cols = list(column_mapping.values()) + ['id']
if set(powerbi_cols).issubset(set(powerbi_data.columns)):
    powerbi_data = powerbi_data[powerbi_cols]
else:
    # Handle missing columns
    available_cols = [col for col in powerbi_cols if col in powerbi_data.columns]
    powerbi_data = powerbi_data[available_cols]

# Save for dashboard tools
powerbi_data.to_csv('../data/processed/dashboard_data/mental_health_powerbi.csv', index=False)

print("Dashboard data preparation complete! Files saved to data/processed/dashboard_data/")