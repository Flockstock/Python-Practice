import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo

#fetch dataset
print("Starting download ...", flush= True)
online_retail = fetch_ucirepo(id = 352)
print("Dataset loaded!" , flush = True)

X = online_retail.data.features
y = online_retail.data.targets
# Check the data 
print("\n First five rows")
print (X.head())
# Check the size
print("DATASET OVERVIEW")
print("Dataset shape:" , X.shape)

# columns as list
print("\n Column names:")
print(X.columns.tolist())

#missing values
print("\n Missing values per column")
print(X.isnull().sum())

## Analysing Quantities and prices
quantity = X["Quantity"].to_numpy()
prices = X["UnitPrice"].to_numpy()

print("\n NUMPY ANALYSIS")
print("Average quantity:", np.mean(quantity))
print("Median quantity:", np.median(quantity))
print("Total quantity:" , np.sum(quantity))
print("Minimum quantity:" ,np.min(quantity))
print("Maximum quantity:" , np.max(quantity))

print("\n PRICE ANALYSIS")
print("Average price:", np.mean(prices))
print("Median price:" , np.median(prices))
print("Total price:", np.sum(prices))
print("Maximum price:", np.max(prices))
print("Minimum price:", np.min(prices))

print("\nData Checks")
print("Negative Quantity Records:" , np.sum(quantity < 0))
print("Zero-price records:", np.sum(prices == 0))
print("Negative price records:" , np.sum(prices < 0))

















