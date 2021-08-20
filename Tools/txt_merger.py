import os, glob, json, exporter, preparing, datetime
import pandas as pd
import vaex
import time
from time import time

import numpy as np
import matplotlib.pyplot as plt
'''
mypath = "/Users/GabrielaA/Documents/GitHub/Coinmetrics/Data"

data_files = glob.glob(os.path.join(mypath, 'data_dump_monthly.json'))

data = vaex.from_json(data_files[0])

print(data[0][1])
#time.sleep(10000)
pandas_df = data.to_pandas_df()
print(pandas_df)

pandas_df.plot(x= 'timestamp', y= 'price', kind = 'scatter')
plt.show()

'''
mypath = "/Users/GabrielaA/Documents/GitHub/Coinmetrics/Data"

data =pd.DataFrame()
##### to change: load only 1 year for 4 exchanges ###

for file in glob.glob(os.path.join(mypath, 'data_dump_monthly_*.txt')):
    data = pd.concat([data,vaex.from_json(file).to_pandas_df()])
    print("100% negga!")

#print(data[0][1])
#print(data[0])
'''
#load all files, save as json, open the json, convert to pandas df, export to binary file
with open('Data/full_bitstamp_dump.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True, default=str)

with open('Data/full_bitstamp_dump.txt') as json_file:
    mydata = json.load(json_file)
'''

#h5File = "bitstamp_full.hdf5"
#pandas_df.to_hdf(h5File, "/Users/GabrielaA/Documents/GitHub/Coinmetrics/Data/bitstamp")
#pandas_df = data.to_pandas_df()

###create dictionary:

dict = { "timestamp" : 0, "price" : 1, "amount" : 2, "market" : 3}

data[dict["timestamp"]]
#data.to_stata('final.dta') 
#print(data)

