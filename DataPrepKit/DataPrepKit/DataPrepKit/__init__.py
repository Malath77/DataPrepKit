#Data Reading

import pandas as pd


def read_data(file_path, file_format='csv'):
    if file_format == 'csv':
        return pd.read_csv(file_path)
    elif file_format == 'excel':
        return pd.read_excel(file_path)
    elif file_format == 'json':
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Supported formats are: 'csv', 'excel', 'json'.")



#Data Summary
import numpy as np

def data_summary(data):
   numeric_data = data.select_dtypes(include=[np.number])  # Select numeric columns only
   summary = {}
   summary['mean'] = numeric_data.mean()
   summary['median'] = numeric_data.median()
   summary['mode'] = numeric_data.mode().iloc[0]
   summary['standard_deviation'] = numeric_data.std()
   summary['max'] = numeric_data.max()
   summary['min'] = numeric_data.min()
   return summary



#print(summary)
#Handling Missing Values
def handle_missing_values(data, strategy='remove'):
    if strategy == 'remove':
        return data.dropna()
    elif strategy == 'mean_impute':
        return data.fillna(data.mean())
    elif strategy == 'median_impute':
        return data.fillna(data.median())
    elif strategy == 'mode_impute':
        return data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Unsupported missing value handling strategy. Supported strategies are: 'remove', 'mean_impute', 'median_impute', 'mode_impute'.")


#Categorical Data Encoding
def encode_categorical_data(data):
    return pd.get_dummies(data)