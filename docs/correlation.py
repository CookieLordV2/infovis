# Calculate all possible Pearson's R

import pandas as pd
from scipy.stats import pearsonr
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('train_age_dataset.csv')
list_corr = []

for column in df.columns:
    for target_column in df.columns:
        if column != target_column:
            df_cleaned = df.dropna(subset=[column, target_column])

            # Extract the two attributes as separate Series from the DataFrame
            x = df_cleaned[column]
            y = df_cleaned[target_column]
            # Calculate Pearson's correlation coefficient and p-value
            corr, p_value = pearsonr(x, y)

            # Print the correlation coefficient
            list_corr.append([corr, column, target_column])
            #print("Pearson's correlation coefficient:", corr)

list_corr.sort()

list_corr = list_corr[::2]

print(list_corr)