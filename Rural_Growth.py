import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

df=pd.read_csv('D:/rektorov_rad/programirano/Ruralno/460271f3-8ed4-46fa-bcc5-726c768a8db8_Data.csv')
#print(df.iloc[:-5,2:-1])

df=df.iloc[:-5,2:-1]

df.columns=['Country Name', 'Country Code', '1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']

world = df[df['Country Name']=='World']
#print(world)
df=df.iloc[:-47,:]
#print(df.tail())

#print(df.shape)

def stringops(text):
    if text=='..':
        return None
    else:
        return text

for i in df.columns:
    df[i]=df[i].apply(stringops)

df=df.dropna()

#print(df.isnull().sum())

lista=['1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']

for i in lista:
    df[i]=pd.to_numeric(df[i])

#print(df.dtypes)

#print(df.shape)

df=df.sort_values(by='2019', ascending=False)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Highest) Population Growth in rural areas in %')
fig.show()

df=df.sort_values(by='2019', ascending=True)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Lowest) Population Growth in rural areas in %')
fig.show()


# WORLD
for i in lista:
    world[i]=pd.to_numeric(world[i])

world=world.T
world=world.iloc[2:,:]
print(world)
year=world.index.tolist()
data=world.iloc[:,0].tolist()
print(data)
fig=px.bar(y=data,x=year,color=year,
       template='plotly_dark',title='World Population Growth in rural areas in %',
       labels=dict(x="Years", y="Population Growth in rural areas in %", color="Years"))
fig.show()
fig=px.line(y=data,x=year,
       template='plotly_dark',title='World Population Growth in rural areas in %',
       labels=dict(x="Years", y="Population Growth in rural areas in %"))
fig.show()

def specific_country(country_name):
    country_data = df[df['Country Name']==country_name]
    country_data=country_data.T
    country_data=country_data.iloc[2:,:]
    year=country_data.index.tolist()
    data=country_data.iloc[:,0].tolist()
    fig=px.bar(y=data,x=year,color=year,
           template='plotly_dark',title=country_name+' Population in largest city',
           labels=dict(x="Years", y="Population in largest city", color="Years"))
    fig.show()
    fig=px.line(y=data,x=year,
           template='plotly_dark',title=country_name+' Population in largest city',
           labels=dict(x="Years", y="Population in largest city"))
    fig.show()

a=input('Your Country Name: __ ')

try:
    specific_country(a)
except:
    print('Invalid Country Name')


df=df.sort_values(by='2019', ascending=False)

df = pd.melt(df, id_vars=['Country Name', 'Country Code'], value_vars=lista)
print(df)
fig = px.choropleth(df,                            # Input Dataframe
                     locations="Country Code",           # identify country code column
                     color="value",                     # identify representing column
                     hover_name="Country Name",              # identify hover name
                     animation_frame="variable",        # identify date column
                     projection="natural earth",        # select projection
                     color_continuous_scale = 'Peach',  # select prefer color scale
                     range_color=[-6,6]              # select range of dataset
                     )        
fig.show()
