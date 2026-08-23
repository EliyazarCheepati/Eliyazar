import pandas as pd

# Your Excel dataset
file_path = r"C:\Users\HP\OneDrive\Documents\StudentPerformanceFactors.csv.xlsx"

# Read Excel file
df = pd.read_excel(file_path)

print("\n======================================")
print("DATASET LOADED SUCCESSFULLY")
print("======================================")

print("\nFirst 5 rows:")
print(df.head())

print("\n======================================")
print("DATASET SHAPE")
print("======================================")

print(df.shape)

print("\n======================================")
print("COLUMN NAMES")
print("======================================")

print(df.columns.tolist())

print("\n======================================")
print("DATA TYPES")
print("======================================")

print(df.dtypes)

print("\n======================================")
print("MISSING VALUES")
print("======================================")

print(df.isnull().sum())

print("\n======================================")
print("DUPLICATE ROWS")
print("======================================")

print(df.duplicated().sum())