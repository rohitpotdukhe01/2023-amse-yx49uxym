import pandas as pd
import sqlite3

#Fetch and load data into a dataframe
url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
df = pd.read_csv(url, delimiter=";", encoding='iso-8859-1', skiprows=6, skipfooter=4, engine='python')

#Columns to keep and renaming them as follows
df.columns.values[0] = 'date'
df.columns.values[1] = 'CIN'
df.columns.values[2] = 'name'
df.columns.values[12] = 'petrol'
df.columns.values[22] = 'diesel'
df.columns.values[32] = 'gas'
df.columns.values[42] = 'electro'
df.columns.values[52] = 'hybrid'
df.columns.values[62] = 'plugInHybrid'
df.columns.values[72] = 'others'

columns_to_keep = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

#Drop the remaining columns
df = df[columns_to_keep]
#print(df.head())

#Validate data
#CINs are Community Identification Numbers, must be strings with 5 characters and can have a leading 0
df['CIN'] = df['CIN'].astype(str).str.zfill(5)

#all other columns should be positive integers > 0
numeric_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

numeric_df = df[(df[numeric_columns] != '-')]
df[numeric_columns] = numeric_df[numeric_columns]
df = df.dropna()
df[numeric_columns] = df[numeric_columns].astype(int)

#drop all rows that contain invalid values
positive_df = df[(df[numeric_columns] > 0)]
df[numeric_columns] = positive_df[numeric_columns]
df = df.dropna()

#Write data into a SQLite database
df.to_sql("cars", "sqlite://" + "/cars.sqlite", if_exists='replace', index=False)








