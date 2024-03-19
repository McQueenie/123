import pandas as pd
import numpy as np

# generates random: Height, Weight, BMI, Cholesterol LDL, Cholesterol HDL, Gender, Age
# based on file from J Drapała
def generate_data(rows):
    file_path = 'app/static/data/test_data/cardiac_patients.xlsx'
    df = pd.read_excel(file_path)

    prob_distributions = {}
    for column in df.columns:
        if column != 'Gender' or column != 'BMI':
            prob_distributions[column] = df[column].value_counts(normalize=True)

    new_data = pd.DataFrame()
    for column, distribution in prob_distributions.items():
        new_column_values = np.random.choice(distribution.index, size=rows, p=distribution.values)
        new_data[column] = new_column_values

    new_data['Gender'] = np.random.choice(['Male', 'Female'], size=rows)
    new_data['BMI'] = new_data['Weight'] / ((new_data['Height'] / 100) ** 2)

    return new_data
