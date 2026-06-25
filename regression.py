import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
train_df = pd.read_csv(r'C:\Users\HP\Downloads\train.csv')
train_df.head()
print(train_df.head())
print(train_df['SalePrice'].mean())