import pandas as pd
df=pd.read.csv("Titanic-Dataset.csv")
print(df.head())
print(df.info())

# Step 4: Summary of numerical columns
print(df.describe())

# Step 5: Count missing values in each column
print(df.isnull().sum())

# Step 6: Check dataset shape (rows, columns)
print("Shape of dataset:", df.shape)
