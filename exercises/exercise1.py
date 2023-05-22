import pandas as pd
#import sqlalchemy as sq
from sqlalchemy.types import Float, Text, Integer, String

#Fetch and load data into a dataframe
url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
df = pd.read_csv(url, delimiter=';', index_column='column_1')
#print(df.head())

columns_dataTypes = {
    "column_1": Integer,
    "column_2": String,
    "column_3": Text,
    "column_4": Text,
    "column_5": String(3),
    "column_6": String(4),
    "column_7": Float,
    "column_8": Float,
    "column_9": Integer,
    "column_10": Float,
    "column_11": Text(1),
    "column_12": String,
    "geo_punkt": String
}

df.to_sql("airports", "sqlite://" + "/airports.sqlite", if_exists='replace', dtype=columns_dataTypes)

