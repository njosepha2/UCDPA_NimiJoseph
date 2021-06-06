import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Importing the data set from our location using pandas.
df=pd.read_csv("/home/markv/Downloads/gg/covid_19_india.csv")
print(df.head(10))
print(df.shape)

# Performing preliminary analysis.
print(df.info())
print(df.describe())
# Performing data cleaning.
print(df.isnull().sum())

# Assigning the original data frame to new data frame before performing any modification.
dataFrame=df
dataFrame.Sno = dataFrame.Sno.fillna('0')
dataFrame.Date = dataFrame.Date.fillna('0')
dataFrame.Time = dataFrame.Time.fillna('0')
dataFrame.Cured = dataFrame.Cured.fillna('0')
dataFrame.Deaths = dataFrame.Deaths.fillna('0')
dataFrame.Confirmed = dataFrame.Confirmed.fillna('0')
del dataFrame["ConfirmedIndianNational"]
del dataFrame["ConfirmedForeignNational"]
print(dataFrame.isnull().sum())