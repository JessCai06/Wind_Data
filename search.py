import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

df = pd.read_csv("Wind Farm Data - All data.csv")
indices = [i for i in range(0, 167)]
#print(indices)
df = df.assign(index = indices)
df.set_index('index', inplace=True)



"""
# Drop strings
hidden_col = ["tempmax", "tempmin" , "temp","name", 'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'humidity', 
                      'precip', 'precipprob', 'precipcover', 'preciptype', 'snow', 
                      'snowdepth', 'sealevelpressure', 'cloudcover', 'visibility', 
                      'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 
                      'sunrise', 'sunset', 'moonphase', 'conditions', 'description', 
                      'icon', 'stations', "description", "icon", "stations"]
df.drop(hidden_col, axis=1, inplace=True)
"""
print(df)

"""
needed_col = ['windgust', 'winddir','windspeed']
monthly_averages = df[needed_col].resample('M').mean()
moving the data to csv
monthly_averages.to_csv('monthly_averages2.csv')
"""
