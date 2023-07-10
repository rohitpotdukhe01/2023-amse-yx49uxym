import os
import urllib.request
import zipfile
import pandas as pd
from sqlalchemy.types import Integer, Text, Float

url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
file_path = "GTFS.zip"
file_name = "stops.txt"
column_picker = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]
columns_dType = {"stop_id" : Integer, "stop_name" : Text, "stop_lat" : Float, "stop_lon" : Float, "zone_id" : Integer}

# zipfile processing
filehandle, _ = urllib.request.urlretrieve(url, file_path)
zip_obj = zipfile.ZipFile(filehandle)
stops_file = zip_obj.open(file_name)
df = pd.read_csv(stops_file, encoding= 'ISO-8859-1')


# Pick out only stops (from stops.txt)
df = df[column_picker]

# Only keep stops from zone 2001
df = df[df["zone_id"] == 2001]

# validate data
df = df[(df["stop_lat"] >= -90) & (df["stop_lat"] <= 90) & (df["stop_lon"] >= -90) & (df["stop_lon"] <= 90)]

# Write data into a SQLite database, and set the correct data types
df.to_sql("stops", "sqlite://" + "/gtfs.sqlite", if_exists='replace', dtype=columns_dType, index=False)