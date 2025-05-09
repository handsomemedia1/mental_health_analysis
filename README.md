![image](https://github.com/user-attachments/assets/946c24a7-ac44-45af-8faf-a1127bb577bf)﻿# mental_health_analysis
Mental Health in Tech: Data Analysis & Visualization
Project Overview
This project analyzes mental health benefits, resources, and discussion comfort levels in the tech industry from 2014-2019, based on survey data. Using Python, R, and machine learning techniques, the analysis explores trends in workplace mental health support and identifies key factors that predict employee comfort in discussing mental health issues.
Motivation
Mental health concerns are prevalent in the fast-paced tech industry, yet the availability of resources and comfort in discussing these concerns varies widely across organizations. This analysis aims to quantify these variations and identify actionable insights for improving mental health support in the workplace.
Dataset
The analysis uses the "Mental Health in Tech Survey 2014-2019" dataset, which contains responses from tech professionals regarding:

Company size and type (tech vs. non-tech)
Mental health benefits availability
Awareness of benefits
Comfort discussing mental health with coworkers and supervisors
Employer-provided mental health resources

Project Structure
mental_health_analysis/
│
├── data/
│   ├── raw/
│   │   └── Mental health in tech survey 2014-2019.csv
│   ├── processed/
│   │   ├── mental_health_tech_cleaned.csv
│   │   ├── mental_health_tech_analyzed.csv
│   │   └── model_predictions.csv
│   └── dashboard_data/
│       ├── yearly_trends.csv
│       ├── company_size_analysis.csv
│       ├── tech_vs_nontech.csv
│       ├── employment_type.csv
│       ├── correlation_matrix.csv
│       └── mental_health_powerbi.csv
│
├── notebooks/
│   ├── 1.0-data-exploration.ipynb
│   ├── 2.0-data-cleaning.ipynb
│   ├── 3.0-exploratory-data-analysis.ipynb
│   └── 4.0-predictive-modeling.ipynb
│
├── scripts/
│   └── prepare_dashboard_data.py
│
├── models/
│   └── mental_health_predictor.pkl
│
├── reports/
│   ├── figures/
│   │   ├── responses_by_year.png
│   │   ├── benefits_trend.png
│   │   ├── tech_vs_nontech.png
│   │   └── ml/
│   │       ├── confusion_matrix.png
│   │       └── feature_importance.png
│   └── executive_summary.md
│
├── visualizations/
│   ├── tableau_dashboard.twbx
│   └── powerbi_dashboard.pbix
│
└── README.md
Methodology
1. Data Cleaning

Standardized text responses
Handled missing values
Created binary indicators for key metrics
Normalized categorical variables

2. Exploratory Data Analysis

Analyzed trends in mental health benefits over time (2014-2019)
Investigated the relationship between company size and benefit availability
Compared tech vs. non-tech companies in mental health support
Examined employee comfort levels in discussing mental health issues

3. Statistical Analysis

Performed hypothesis testing to identify significant associations
Analyzed correlation between workplace factors and mental health discussion comfort
Identified key predictors of mental health benefits availability

4. Predictive Modeling

Developed a Random Forest classifier to predict employee comfort in discussing mental health
Evaluated model performance using cross-validation
Identified the most important features influencing employee comfort

5. Visualization

Created interactive dashboards in Tableau and Power BI
Developed time-series visualizations of mental health metrics
Generated comparative visualizations across company sizes and types

Key Findings

Benefit Availability Trends:

Uploading image.png…

Company size significantly impacts the availability of mental health benefits


Tech vs. Non-Tech Companies:

![image](https://github.com/user-attachments/assets/03a01ada-bf94-43b2-9f1e-2e3180a018ad)

Tech companies are [less] likely to offer mental health benefits than non-tech companies


Comfort Level Predictors:

The strongest predictors of employee comfort discussing mental health are:

![image](https://github.com/user-attachments/assets/2cc3f909-851c-4e54-948a-1c426c404612)

Employer-initiated discussions about mental health
Availability of learning resources




Model Insights:

Our predictive model achieved 0.6685% accuracy in predicting employee comfort levels
Feature importance analysis revealed that were most influential



Tools and Technologies Used

Programming Languages: Python, R
Data Analysis Libraries: pandas, NumPy, scikit-learn
Visualization: Matplotlib, Seaborn, Tableau, Power BI
Machine Learning: RandomForest Classifier
Development Environment: Jupyter Notebooks, VS Code

Setup and Installation

Clone the repository

git clone https://github.com/yourusername/mental_health_analysis.git
cd mental_health_analysis

Create a virtual environment and install dependencies

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt

Place the dataset file in the data/raw/ directory

Mental health in tech survey 2014-2019.csv
Running the Analysis
Execute the notebooks in sequence:

Data Exploration

jupyter notebook notebooks/1.0-data-exploration.ipynb

Data Cleaning

jupyter notebook notebooks/2.0-data-cleaning.ipynb

Exploratory Data Analysis

jupyter notebook notebooks/3.0-exploratory-data-analysis.ipynb

Predictive Modeling

jupyter notebook notebooks/4.0-predictive-modeling.ipynb

Dashboard Data Preparation

python scripts/prepare_dashboard_data.py
Visualizations
The project includes interactive dashboards created with Tableau and Power BI:

Benefits Analysis Dashboard: Examines trends in mental health benefits across companies
Comfort Level Dashboard: Visualizes factors affecting employee comfort in discussing mental health
Predictive Insights Dashboard: Showcases model results and feature importance

Future Work

Expand analysis to include more recent data (post-2019)
Develop region-specific insights by incorporating geographical data
Analyze the impact of COVID-19 on mental health support in tech companies
Implement more advanced NLP techniques for analyzing open-ended survey responses

Contact Information
Elijah Adeyeye
Email: [elijahadeyeye@proton.me]
LinkedIn: https://www.linkedin.com/in/adeyeye-elijah/
GitHub: https://github.com/handsomemedia1/mental_health_analysis

License
This project is licensed under the MIT License - see the LICENSE file for details.
