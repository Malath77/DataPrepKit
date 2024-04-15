import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

class DataHandler:
    def _init_(self):
        pass

    def read_file(self, file_format, file_path):
        if file_format == 'csv':
            df = pd.read_csv(file_path)
        elif file_format == 'xlsx':
            df = pd.read_excel(file_path)
        elif file_format == 'json':
            df = pd.read_json(file_path)
        else:
            raise ValueError("Please provide a valid format (csv, excel, json)")
        return df

    def data_summary(self, df):
        print("Data Summary:")
        print("Number of Rows:", df.shape[0])
        print("Number of Columns:", df.shape[1])

        for column in df.columns:
            if pd.api.types.is_numeric_dtype(df[column]):
                print(f"Average Values [{column}]: {df[column].mean()}")
                print(f"Most Frequent Value [{column}]: {df[column].mode().iloc[0]}")
                print(f"Standard Deviation [{column}]: {df[column].std()}")
                print(f"Median [{column}]: {df[column].median()}")
                print(f"Minimum Value [{column}]: {df[column].min()}")
                print(f"Maximum Value [{column}]: {df[column].max()}")
                print(f"Skewness [{column}]: {df[column].skew()}")
            else:
                print(f"Count of unique values in [{column}]: {df[column].nunique()}")

    def handle_missing_values(self, df, strategy='remove', column=None, value=None):
        if strategy == 'remove':
            df = df.dropna()
        elif strategy == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif strategy == 'median':
            df[column].fillna(df[column].median(), inplace=True)
        elif strategy == 'custom_value':
            df[column].fillna(value, inplace=True)
        else:
            raise ValueError("Please choose from 'remove', 'mean', 'median', 'custom_value'.")
        return df

    def handle_missing(self, df):
        print("Handling Missing Values:")
        print("1. Remove rows with missing values")
        print("2. Impute missing values with mean")
        print("3. Impute missing values with median")
        print("4. Impute missing values with a custom value")

        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            df = self.handle_missing_values(df, strategy='remove')
        elif choice == '2':
            column = input("Enter the column name to impute missing values with mean: ")
            df = self.handle_missing_values(df, strategy='mean', column=column)
        elif choice == '3':
            column = input("Enter the column name to impute missing values with median: ")
            df = self.handle_missing_values(df, strategy='median', column=column)
        elif choice == '4':
            column = input("Enter the column name to impute missing values with a custom value: ")
            custom_value = input("Enter the custom value: ")
            df = self.handle_missing_values(df, strategy='custom_value', column=column, value=custom_value)
        else:
            print("Invalid choice. Please choose from 1, 2, 3, or 4.")
        return df

    def categorical_data_encoding(self, df):
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
        for column in categorical_columns:
            df[column] = df[column].astype('category').cat.codes
        return df

    def main(self):
        file_path = input("Please enter the path of your file: ")
        file_format = file_path.split('.')[-1]
        df = self.read_file(file_format, file_path)
        print("Represent of the file:")
        print(df)

        self.data_summary(df)

        df = self.handle_missing(df)

        df = self.categorical_data_encoding(df)

        print("Final DataFrame:")
        print(df)
        self.data_summary(df)


# Instantiate and run the main function
handler = DataHandler()
handler.main()