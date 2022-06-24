import pandas as pd

date = "MOD_NDVI_M_2000-03.CSV"
#       Year- Month

newDate = pd.to_datetime(date, format="MOD_NDVI_M_%Y-%m.CSV")

print(date)
print(newDate)
