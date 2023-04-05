# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:11:20 2023

@author: User
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Creating a def function to read in our datasets and returns  two 
dataframes:one with years as columns, the other with nations
"""

def read_climate_data (filename, **others):
    """
    A function that reads in climate change data alongside various indicators from 
    the world bank database and returns both the original and transposed version of
    the dataset
    
    Args:
        filename: the name of the world bank data that will be read for analysis 
        and manupulation
        
        **others: other arguments to pass into the functions as need be
            
    Returns: 
        The original dataset format as obtained from the world bank and its transposed version
    """        
# Read the World Bank data into a dataframe
    df_climate_data = pd.read_csv(filename, skiprows=4)
# Transpose the dataframe and set the country code as the index
    df_years = df_climate_data.drop(['Country Code', 'Indicator Code'], axis=1)
    df_countries = df_climate_data.drop(['Country Name', 'Country Code', 'Indicator Code'], axis=1).set_index(df_climate_data['Country Name']).T.reset_index().rename(columns={'index': 'Year'})
    df_countries = df_countries.set_index('Year').dropna(axis=1)
    

    return df_years, df_countries
df_years, df_countries = read_climate_data("API_19_DS2_en_csv_v2_5361599.csv")
print(df_countries)

#df_years = df_years.apply(pd.to_numeric)  # converting to data type to a numeric format
print(df_years)

#Define indicators and countries
indicators = df_years[df_years['Indicator Name'].isin(["Urban population", "Population, total", "Agricultural land (% of land area)", "Arable land (% of land area)"])]
countries = ['United States', 'China', 'Australia', 'Germany', 'Italy', 'United Kingdom', 'Nigeria', 'France', 'Canada', 'Japan']
selected_countries = indicators[indicators['Country Name'].isin(countries)]
selected_countries = selected_countries.dropna(axis=1)
selected_countries = selected_countries.reset_index(drop=True)
countries_years = selected_countries[['Country Name','Indicator Name','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2006']]
selected_countries = countries_years

print(selected_countries)

stats_desc = selected_countries.groupby(["Country Name", "Indicator Name"])
stats_desc.describe()

#  calculate the summary statistics of each group
summary_stats_others = selected_countries.groupby(['Country Name', 'Indicator Name'])
for name, group in summary_stats_others:
    print(name)
    print('Mean:', group.mean()['1990':'2006'])
    print('Min:', group.min()['1990':'2006'])
    print('Max:', group.max()['1990':'2006'])
    print('Median:', group.median()['1990':'2006'])
    print('Standard deviation:', group.std()['1990':'2006'])
    print('Standard deviation:', group.select_dtypes(include='number').std()['1990':'2006'])
 
    
    
#select data for Urban Population indicator
Urban_pop = selected_countries[selected_countries["Indicator Name"] == "Urban population"]
Urban_pop = Urban_pop.set_index('Country Name', drop=True)
Urban_pop= Urban_pop.transpose().drop('Indicator Name')
Urban_pop[countries] = Urban_pop[countries].apply(pd.to_numeric, errors='coerce', axis=1)
print(Urban_pop)

#select data for Total Population indicator
Pop_tot = selected_countries[selected_countries["Indicator Name"] == "Population, total"]
Pop_tot = Pop_tot.set_index('Country Name', drop=True)
Pop_tot= Pop_tot.transpose().drop('Indicator Name')
Pop_tot[countries] = Pop_tot[countries].apply(pd.to_numeric, errors='coerce', axis=1)
Pop_tot

#select data for Agricultural land indicator
Agric_land = selected_countries[selected_countries["Indicator Name"] == "Agricultural land (% of land area)"]
Agric_land = Agric_land.set_index('Country Name', drop=True)
Agric_land= Agric_land.transpose().drop('Indicator Name')
Agric_land[countries] = Agric_land[countries].apply(pd.to_numeric, errors='coerce', axis=1)
print(Agric_land)

#select data for Arable land indicator
Arab_land = selected_countries[selected_countries["Indicator Name"] == "Arable land (% of land area)"]
Arab_land = Arab_land.set_index('Country Name', drop=True)
Arab_land= Arab_land.transpose().drop('Indicator Name')
Arab_land[countries] = Arab_land[countries].apply(pd.to_numeric, errors='coerce', axis=1)
print(Arab_land)

# Plot the data as a line plot

# Create a line plot of the Agric_land DataFrame
Agric_land.plot.line(figsize=(10, 6))
plt.title('Agricultural Land (% of Land Area) in Selected Countries')
plt.xlabel('Year')
plt.ylabel('Percentage of Land Used for Agriculture')
plt.legend(title='Countries')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.savefig('lineplot.png', dpi=300)

plt.show()

# Create a line plot of the Urban_pop DataFrame
Urban_pop.plot.line(figsize=(10, 6))
plt.title('Urban Population in Selected Countries')
plt.xlabel('Year')
plt.ylabel('Urban Population')
plt.legend(title='Countries')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('lineploturb.png')

plt.show()


# Plot the data as a bar plot for Population total
fig, ax = plt.subplots(figsize=(10, 6))
Pop_tot.T.plot(kind='bar', ax=ax)

# Set the x-axis and y-axis labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Population, total')
ax.set_title('Population, total')

# Add legend to the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.savefig('barplotpop.png')

plt.show()

# Plot the data as a bar plot for Population total
fig, ax = plt.subplots(figsize=(10, 6))
Arab_land.T.plot(kind='bar', ax=ax)

# Set the x-axis and y-axis labels and title
ax.set_xlabel('Year')
plt.ylabel("Arable land (% of land area)")
ax.set_title('Arable land')
plt.style.use('classic')


# Add legend to the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.savefig('barplot.png')
plt.show()

# Define the data for the heatmap
United_States = pd.DataFrame({
    'Agricultural land': Agric_land['United States'], 
    'Urban population': Urban_pop['United States'],
    'Arable land (% of land area)': Arab_land['United States'], 
    'Population, total': Pop_tot['United States']
}, index=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006'])

# Calculate the correlation matrix
corr_matrix = United_States.corr()

# Create a heatmap of the correlation matrix
plt.figure(figsize=(8,5))
heatmap = plt.imshow(corr_matrix, cmap='Greens')
plt.title('Correlation heatmap United States')
plt.colorbar(heatmap)
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

# Add annotations to the heatmap
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        text = '{:.2f}'.format(corr_matrix.iloc[i, j])
        plt.text(j, i, text, ha='center', va='center', color='black')

# Save the plot as a PNG image
plt.savefig('heatmap.png', dpi=300)

# Show the plot in the console or in a separate window
plt.show()


# Define the data for the heatmap
China = pd.DataFrame({
    'Agricultural land': Agric_land['China'], 
    'Urban population': Urban_pop['China'],
    'Arable land (% of land area)': Arab_land['China'], 
    'Population, total': Pop_tot['China']
}, index=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006'])

# Calculate the correlation matrix
corr_matrix = China.corr()

# Create a heatmap of the correlation matrix
plt.figure(figsize=(8,5))
heatmap = plt.imshow(corr_matrix, cmap='Blues')
plt.title('Correlation heatmap China')
plt.colorbar(heatmap)
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

# Add annotations to the heatmap
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        text = '{:.2f}'.format(corr_matrix.iloc[i, j])
        plt.text(j, i, text, ha='center', va='center', color='black')

# Save the plot as a PNG image
plt.savefig('heatmap.png', dpi=300)

# Show the plot in the console or in a separate window
plt.show()


