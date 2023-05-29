import pandas as pd
import sqlite3

# #Fetch and load dataset 1
url1 = "https://offenedaten-koeln.de/sites/default/files/Fahrrad_Zaehlstellen_Koeln_2020.csv"
df_2020 = pd.read_csv(url1, encoding="iso-8859-1",  delimiter=';')

# #Fetch and load dataset 2
url2 = "https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202021.csv"
df_2021 = pd.read_csv(url2, encoding="iso-8859-1",  delimiter=';')

# #Fetch and load dataset 3
url3 = "https://offenedaten-koeln.de/sites/default/files/Radverkehr%20f%C3%BCr%20Offene%20Daten%20K%C3%B6ln%202022.csv"
df_2022 = pd.read_csv(url3, encoding="iso-8859-1",  delimiter=';')

#Connect and load into SQLite database
connection = sqlite3.connect('AMSE_database.db')

df_2022.to_sql("Bicycle_Traffic_Data_Cologne_2022", connection, if_exists='replace', index=False)
df_2021.to_sql("Bicycle_Traffic_Data_Cologne_2021", connection, if_exists='replace', index=False)
df_2020.to_sql("Bicycle_Traffic_Data_Cologne_2020", connection, if_exists='replace', index=False)

connection.commit()
connection.close()