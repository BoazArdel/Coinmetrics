import requests
import json
#from coinmetrics.api_client import CoinMetricsClient
#from coinmetrics.constants import PagingFrom
import collections
from collections import Counter
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import tkinter as tk
from tkinter import filedialog
from passwords import API_KEY

'''
response = requests.get('https://api.coinmetrics.io/v4/catalog-all/exchanges?pretty=true&api_key=' + API_KEY).json()
response = requests.get('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2014-07-17T08:00:00.000000000Z&paging_from=start&markets=bitfinex-btc-usd-spot&pretty=true&api_key=' + API_KEY).json()
response = requests.get('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2014-07-17T08:00:00.000000000Z&paging_from=start&markets=kraken-btc-usd-spot&pretty=true&api_key=' + API_KEY).json()
response = requests.get('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2014-07-17T08:00:00.000000000Z&paging_from=start&markets=bitstamp-btc-usd-spot&pretty=true&api_key=' + API_KEY).json()

print(response)
exit()
'''
#indexes request:
#'bitfinex-btc-usd-spot': 'min_time': '2013-01-14T16:47:23.000000000Z', 'max_time': '2020-08-24T15:03:57.789000000Z'}
#'kraken-btc-usd-spot': 'min_time': '2013-09-10T23:47:11.546000000Z', 'max_time': '2020-08-24T15:03:57.665179000Z'}
#'bitstamp-btc-usd-spot':'min_time': '2011-08-18T12:37:25.000000000Z', 'max_time': '2020-08-24T15:03:53.181000000Z'}



#mydata = {"kraken" : [], "finex" : [], "bitstamp" : []}
mydata = {"kraken" : [], "finex" : [], "bitstamp": []}
def getDataByEndDate(url,selected_date):
    data = []
    response = requests.get(url).json()
    for i in range(0,10000):   #by dates
        if(response["data"][0]["time"]>selected_date): break
        out_file = open("exampleorder.json", "w")
        out_file.write(json.dumps(response, indent=4, sort_keys=True))
        out_file.close()
        #print(json.dumps(response, indent=4, sort_keys=True))
        for datagram in response["data"]:
                for bid in datagram["bids"]:
                    data.append({"timestamp": datetime.datetime.strptime(datagram["time"], '%Y-%m-%dT%H:%M:%S.%f000Z'),"market": datagram["market"], "asks_bids": "bid", "price": bid["price"],"size": bid["size"]})
                for ask in datagram["asks"]:
                    data.append({"timestamp": datetime.datetime.strptime(datagram["time"], '%Y-%m-%dT%H:%M:%S.%f000Z'),"market": datagram["market"], "asks_bids": "ask", "price": ask["price"],"size": ask["size"]})
        response = requests.get(response["next_page_url"]).json()
        print(str(i) + ":" + str(response["data"][0]["time"]))
    #print(json.dumps(data, indent=4, sort_keys=True))
    return data

mydata["kraken"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-orderbooks?start_time=2020-01-17T00:00:00.000000000Z&paging_from=start&markets=kraken-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2020-01-18T00:00:00.000000000Z")


#mydata["kraken"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2015-01-23T00:00:00.000000000Z&paging_from=start&markets=kraken-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2015-01-24T00:00:00.000000000Z")
#mydata["finex"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2019-01-18T00:00:00.000000000Z&paging_from=start&markets=bitfinex-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2019-01-19T00:00:00.000000000Z")
#mydata["bitstamp"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2019-01-18T00:00:00.000000000Z&paging_from=start&markets=bitstamp-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2019-01-19T00:00:00.000000000Z")
##mydata["bitstamp"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2019-01-18T00:00.000000000Z&paging_from=start&markets=bitstamp-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2019-01-20T00:00:00.000000000Z")

#####
df = pd.DataFrame(mydata["kraken"], columns=[ 'timestamp', 'market', 'asks_bids', 'price', 'size'])
df.to_stata('statafile.dta')
print('finished saving')
#df = pd.DataFrame(mydata["kraken"], columns=[ 'timestamp', 'price', 'amount', 'side', 'market'])
#df = pd.DataFrame(mydata["finex"], columns=[ 'timestamp', 'price', 'amount', 'side', 'market'])
#df = pd.DataFrame(mydata["bitstamp"], columns=[ 'timestamp', 'price', 'amount', 'side', 'market'])

'''
root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()


def exportExcel():
    global df

    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel(export_file_path, index=False, header=True)


saveAsButtonExcel = tk.Button(text='Export Excel', command=exportExcel, bg='green', fg='white',
                              font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButtonExcel)

root.mainloop()



#with open('data2.txt', 'w') as outfile:
#    json.dump(mydata, outfile, cls=DateTimeEncoder)
'''

