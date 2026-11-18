#Title: Write a program to import a dataset (CSV/Excel) 
# and display basic information such as shape, 
# data types, and summary statistics.


import pandas as pd

# Import CSV dataset
# df = pd.read_csv("students.csv")
df = pd.read_excel("students.xlsx")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())
