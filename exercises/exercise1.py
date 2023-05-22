import pandas as pd
import sqlalchemy as sq
from sqlalchemy.types import BIGINT, TEXT, FLOAT

#Fetch and load data into a dataframe
url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
df = pd.read_csv(url, delimiter=';')
#print(df.head())

columns_dataTypes = {
    "column_1": sq.Integer,
    "column_2": sq.Text,
    "column_3": sq.Text,
    "column_4": sq.Text,
    "column_5": sq.String(3),
    "column_6": sq.String(4),
    "column_7": sq.Float,
    "column_8": sq.Float,
    "column_9": sq.Integer,
    "column_10": sq.Float,
    "column_11": sq.Text(1),
    "column_12": sq.String,
    "geo_punkt": sq.String}

df.to_sql("airports", "sqlite://" + "/airports.sqlite", if_exists='replace', dtype=columns_dataTypes)

