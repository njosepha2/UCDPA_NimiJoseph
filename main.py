import pandas as pd
import matplotlib.pyplot as plt
# A function called barPlot has been defined here.
def barPlot(covid19_df_latest,columnName,colour):
        plt.figure(figsize=(18, 18), dpi=90)
        plt.bar(covid19_df_latest['State'][:5], covid19_df_latest[columnName][:5],
                align='center', color=colour)
        plt.ylabel("Number of "+columnName+" Cases", size=20)
        plt.title("States with maximum "+columnName+" cases", size=20)
        plt.show()

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
# Renaming the column to better suite our operation and finding the unique value in the new State column.
dataFrame.rename(columns = {'State/UnionTerritory':'State'},inplace=True)
print(dataFrame['State'].unique())
# Plotting a bar graph considering Total Confirmed, Cured, Active and Death cases in the country.

# Plotting a bar graph to see the top five states confirmed covid 19 cases in the country.
covid19_df_latest = dataFrame[dataFrame['Date']=="2021-05-08"]
print(covid19_df_latest.head())
barPlot(covid19_df_latest.sort_values(by=['Confirmed'], ascending = False),"Confirmed","#9e9518")

# Plotting a bar graph to see the top five states cured covid 19 cases in the country.
barPlot(covid19_df_latest.sort_values(by=['Cured'], ascending = False),"Confirmed","green")
