
# Data Cleaning and Exploratory Data Analysis using CSV file

import pandas as pd

# Create CSV file
csv_data = """Name,Department,Attendance,Mark
Asha,CSE,90,88
Bala,CSE,80,76
Charan,ECE,,92
Divya,ECE,95,
Eshan,CSE,85,84
"""

with open("students1.csv", "w") as file:
    file.write(csv_data)

# Choose the CSV file to analyze
filename = "students1.csv"

# Load CSV file
df = pd.read_csv(filename)

print("--- Original Dataset ---")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with column means
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].mean()
)

df["Mark"] = df["Mark"].fillna(
    df["Mark"].mean()
)

# Remove duplicate records
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)

# Descriptive statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Department-wise average marks
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))

# EDA Summary
print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))
