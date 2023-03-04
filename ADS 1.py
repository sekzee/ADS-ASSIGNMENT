
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# loading the dataset into pandas dataframe
df_gdp = pd.read_csv('GDP_per_capita_2015_to_2019_Finland_Norway_Sweden (4).csv')
print(df_gdp)


# Create list of years
column_year = ['2015', '2016', '2017', '2018', '2019']


# A line plot showing multiple lines
plt.figure()

# plot the three countries with labels
plt.plot(column_year, df_gdp["Finland"], label="Finland")
plt.plot(column_year, df_gdp["Norway"], label="Norway")
plt.plot(column_year, df_gdp["Sweden"], label="Sweden")


# Place the labels and show the legend
plt.title('GDP per capita[2015 to 2019]')
plt.xlabel('years')
plt.ylabel('GDP per capita (USD)')

plt.legend()
# save as png
plt.savefig("linplot.png")

plt.show()


# Produce graphs using two other visualisation methods
# Histogram

# create a dictionary with the data
data = {'year': [2015, 2016, 2017, 2018, 2019],
        'Finland': [42802, 43814, 46412, 50038, 48712],
        'Norway': [74356, 70461, 75497, 82268, 75826],
        'Sweden': [51545, 51965, 53792, 54589, 51687]}

# create a Pandas data frame from the dictionary
df = pd.DataFrame(data)

# Input the 'year' column as the index
df.set_index('year', inplace=True)

# select the data for the specified years
years = [2015, 2018, 2017, 2018, 2019]
df = df.loc[years]

# plot a histogram of the GDP per capita for the selected years
df.plot(kind='hist', alpha=0.5, bins=10)

# set the plot title and axis labels
plt.title('GDP per capita (2015-2019)')
plt.xlabel('GDP per capita')
plt.ylabel('Frequency')

# show the plot
plt.show()


# Piechart comparing GDP of two years
# Country with highest GDP in 2018


labels = ['Norway', 'Finland', 'Sweden']
data_gdp = [82268, 50038, 54589]
plt.figure(figsize=(8, 8))
plt.pie(data_gdp, labels=labels, autopct='%1.1f%%')
plt.title('Countries with the Highest GDP in 2018')
plt.legend(loc='best')
plt.show()

#Piechart Comparing the GDP of 2015
#Country with highest GDP in 2015

labels =['Norway', 'Finland', 'Sweden']
data_gdp = [74356,42802 , 51545]
plt.figure(figsize=(8, 8))
plt.pie(data_gdp, labels=labels, autopct='%1.1f%%')
plt.title('Countries with the Highest GDP in 2015')
plt.legend(loc='best')
plt.show()

# save as png
plt.savefig("Piechart.png")


