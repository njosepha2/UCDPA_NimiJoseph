import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# A function called barPlot has been defined here.
def barPlot(covid19_df_latest,columnName,colour):
        plt.figure(figsize=(18, 18), dpi=90)
        plt.bar(covid19_df_latest['State'][:5], covid19_df_latest[columnName][:5],
                align='center', color=colour)
        plt.ylabel("Number of "+columnName+" Cases", size=20)
        plt.title("States with maximum "+columnName+" cases", size=20)
        plt.show()

# A function called fatalityCureRatioPlot has been defined here.
def fatalityCureRatioPlot(covid19_df_latest,columnName,colour):
        plt.figure(figsize=(20,10))
        plt.title(columnName)
        sns.pointplot(data=covid19_df_latest,x='State',y=columnName,color=colour)
        plt.show()

# Importing the data set from our location using pandas.
df=pd.read_csv(r"data/covid_19_india.csv")
print(df.head(10))
print(df.shape)

# Performing preliminary analysis.
print(df.info())
print(df.describe())

#bar chart
x = df['Confirmed'].sum()
y = df['Cured'].sum()
z= df['Deaths'].sum()
active= x-y
print('Total Confirmed cases =',x)
print('Total Cured cases =',y)
print('Total Active cases =',active)
print('Total Death cases =',z)
barp = sns.barplot(x=['Confirmed','Cured','Deaths','active'],y=[x,y,z,active])
barp.set_yticklabels(labels=(barp.get_yticks()*1).astype(int))

#pi chart
data = {'Status': [2085583,6243,1636790]}
pi_chart = pd.DataFrame(data,columns=['Status'],index = ['Confirmed','Deaths','Cured'])
pi_chart.plot.pie(y='Status',figsize=(10, 20),autopct='%1.1f%%', startangle=90)

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
covid19_df_latest_confirmed=covid19_df_latest
barPlot(covid19_df_latest_confirmed.sort_values(by=['Confirmed'], ascending = False),"Confirmed","#9e9518")

# Plotting a bar graph to see the top five states cured covid 19 cases in the country.
covid19_df_latest_cured=covid19_df_latest
barPlot(covid19_df_latest_cured.sort_values(by=['Cured'], ascending = False),"Confirmed","green")

# Indepth analysis of 4 major states
dataFrame=dataFrame.loc[(dataFrame['State'] == 'Kerala') | (dataFrame['State'] == 'Maharashtra')| (dataFrame['State'] == 'Karnataka')|(dataFrame['State'] == 'Tamil Nadu')]

# Here I have plotted a line graph to show both the fatality rate and cure rate.
covid_df1 = dataFrame.tail(2000)
covid_df2 = covid_df1.sort_values(by='Confirmed', ascending=False).head(2000)
covid_df2['Fatality-Ratio'] = covid_df2['Deaths']/covid_df2['Confirmed']
fatalityCureRatioPlot(covid_df2,"Fatality-Ratio","red")
covid_df2['Cure-Ratio'] = covid_df2['Cured']/covid_df2['Confirmed']
fatalityCureRatioPlot(covid_df2,"Cure-Ratio","blue")

# Performed inner join on the two data frames df and gf on the key Date
gf=pd.read_csv(r"data/StatewiseTestingDetails.csv")
merge1= pd.merge(gf,df,how='inner',on='Date')
print(merge1.head())