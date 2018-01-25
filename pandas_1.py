import pandas as pd
from pandas import *
import matplotlib.pyplot as plt

df = pd.read_csv('./Notebooks/data/gapminder.tsv',sep='\t')


print("df.head()")
print(df.head())
print("\n")

print("df.describe().head()")
print(df.describe().head())
print("\n")

country_df = df['country'] # SELECT country FROM df;
print("SELECT country FROM df;")
print(country_df.head())
print("\n")

print("SELECT * FROM df WHERE country='Afghanistan';")
print(df[df.country=='Afghanistan']) # SELECT * FROM df WHERE country="Afghanistan";

print("\n")
subset = df[['country','continent','year']]   #Get only specific columns
print("df[['country','continent','year']] ")
print(subset.head())

print("\n")
print("df.loc[3]")
print(df.loc[3])
print("\n")


print("\n")
print(" df[['country','year','lifeExp']].groupby('country')['lifeExp','year'].max(key='lifeExp').sort_values(ascending= False,by='lifeExp') # Max life expectancy per country")
print( df[['country','year','lifeExp']].groupby('country')['lifeExp','year'].max(key='lifeExp').sort_values(ascending= False,by='lifeExp')) # Max life expectancy per country 


print("\n")
print("df.groupby('year')['lifeExp'].mean() #Average  life expectancy per year")
print(df.groupby('year')['lifeExp'].mean()) #Average  life expectancy per year