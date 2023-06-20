import pandas as pd
import sqlite3

#Fetch and load data into a dataframe
url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
df = pd.read_csv(url, delimiter=";", encoding='iso-8859-1', skiprows=6, skipfooter=4, engine='python')

