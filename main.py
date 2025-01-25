import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the CSV file
data = pd.read_csv('world_population.csv')

# Checking the first few rows of the DataFrame
print("First few rows of the dataset:")
print(data.head())
print("\nBasic statistics of the dataset:")
print(data.describe())

# Histograms for numerical columns
data.hist(figsize=(10, 8))
plt.suptitle('Histograms for Numerical Columns')
plt.show()

# Scatter plot between two chosen columns
plt.figure(figsize=(8, 6))
plt.scatter(data['Column1'], data['Column2'])
plt.xlabel('Rank')
plt.ylabel('CCA3')
plt.title('Scatter plot between Column1 and Column2')
plt.show()

# Correlation matrix
correlation = data.corr()
print("\nCorrelation matrix of the dataset:")
print(correlation)

# Visualization of the correlation matrix
plt.figure(figsize=(12, 10))
plt.matshow(correlation, fignum=1)
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.colorbar()
plt.title('Correlation Matrix')
plt.show()
