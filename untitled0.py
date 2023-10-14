import pandas as pd

# Load data from a CSV file
data = pd.read_csv("C:\\Users\\ccvn5\\PycharmProjects\\New folder\\tt.csv")

# Display the first 5 rows of the data
print(data.head())

# Perform basic statistical analysis
print(data.describe())
