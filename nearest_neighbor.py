import math
import csv
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

"""
the haversine distance formula.
"""
def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


# dot weight = 1/distance
# normalize the weights: percent of weight out of whole: % weight = weight / total weight

df = pd.read_csv("Wind Farm Data - All data.csv")
indices = [i for i in range(0, 167)]
df = df.assign(index = indices)
df.set_index('index', inplace=True)

# constants known to us - this is from the spreadsheets
pap_loc_1 = 27.9958,-97.2967
pap_loc_2 = 27.9386,-97.4586
reader_coordinates = [(27.5, -97.82),(27.55, -97.88), (27.7, -97.5)]

# calculating weight
reader_raw_weights = [1/distance(i,pap_loc_2) for i in reader_coordinates]
print(reader_raw_weights)
reader_normalized_weights = [i/sum(reader_raw_weights) for i in reader_raw_weights]
print(reader_normalized_weights)

# calculating the new weighted wind indicators for the new csv - 
needed_col = ['windgust', 'winddir','windspeed']
dict= {'windgust':[], 'winddir':[],'windspeed':[]}
for c in range(0, len(needed_col)):
    indicator = dict[needed_col[c]]
    for i in range(0, 167):
            weighted = 0.000
            for coord in reader_coordinates:
                colname = str(needed_col[c]) + " - " + str(str(coord)[1:-1])
                #print(colname)
                weighted += reader_normalized_weights[c] * float(df[colname][i])
                #print(str(i)+ " - " + str(reader_normalized_weights) + " " +str(weighted))
            indicator.append(weighted)

#moving the data to csv
DF = pd.DataFrame(dict)
DF.to_csv('weighted_wind_pap2_data.csv')


