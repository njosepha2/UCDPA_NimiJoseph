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