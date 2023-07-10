import os
import urllib.request
import zipfile
import pandas as pd
from sqlalchemy.types import Integer, Text, Float

url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
file_name = "stops.txt"
column_picker = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]
ABS_PATH = os.path.dirname(__file__)

# zipfile processing
filehandle, _ = urllib.request.urlretrieve(url, os.path.join(ABS_PATH, "/GTFS.zip"))
zip_obj = zipfile.ZipFile(filehandle)
stops_file = zip_obj.open(file_name)
df = pd.read_csv(stops_file, encoding= 'ISO-8859-1')
print(df.head())


# # Pick out only stops (from stops.txt)
# df = df[column_picker]
#
# # Only keep stops from zone 2001
# df = df[df["zone_id"] == 2001]
#
# # 2) validate lat/long range
# df = df[df["stop_lat"] <= 90]
# df = df[df["stop_lat"] >= -90]
# df = df[df["stop_lon"] <= 90]
# df = df[df["stop_lon"] >= -90]
#
# # save data to sqlite db, setting the correct types
# df.to_sql("stops", "sqlite://" + "/gtfs.sqlite", if_exists='replace', dtype={
#     "stop_id": Integer,
#     "stop_name": Text,
#     "stop_lat": Float,
#     "stop_lon": Float,
#     "zone_id": Integer}, index=False)