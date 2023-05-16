import pandas as pd
import csv
import sqlite3

#Fetch and load dataset 1
url1 = "https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202022.csv"
df1 = pd.read_csv(url1, delimiter=';', encoding='latin-1')

#Fetch and load dataset 2
url2 = "https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100035541/2019-01.csv"
df2 = pd.read_csv(url2, delimiter=',', encoding='latin-1')

#Connect and load into SQLite database
connection = sqlite3.connect('AMSE_database.db')

df1.to_sql("Bicycle_Traffic_Data_Cologne_2022", connection, if_exists='replace', index=False)
df2.to_sql("Bicycle_Roads_Cologne", connection, if_exists='replace', index=False)

connection.commit()
connection.close()
