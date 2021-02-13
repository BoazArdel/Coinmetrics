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

#binance, coinbase
#response = requests.get('https://api.coinmetrics.io/v4/catalog-all/exchanges?pretty=true&api_key=' + API_KEY).json()
#print(response)
#response = requests.get('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2014-07-17T08:00:00.000000000Z&paging_from=start&markets=binance-btc-usd-spot&pretty=true&api_key=' + API_KEY).json()
#response = requests.get('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2014-07-17T08:00:00.000000000Z&paging_from=start&markets=coinbase-btc-usd-spot&pretty=true&api_key=' + API_KEY).json()


mydata = {"binance" : [], "coinbase" : []}
selected_date = "2020-01-17T00:00:00.000000000Z"
def getDataByEndDate(url,selected_date):
    data = []
    response = requests.get(url).json()
    for i in range(0,10000):   #by dates
        if(response["data"][0]["time"]>selected_date): break
        #print(json.dumps(response, indent=4, sort_keys=True))
        for datagram in response["data"]:
                data.append({"timestamp" : datetime.datetime.strptime(datagram["time"], '%Y-%m-%dT%H:%M:%S.%f000Z'), "amount" : datagram["amount"], "price" : datagram["price"], "side" : datagram["side"], "market" : datagram["market"]})
        response = requests.get(response["next_page_url"]).json()
        print(str(i) + ":" + str(response["data"][0]["time"]))
    #print(json.dumps(data, indent=4, sort_keys=True))
    return data

#mydata["coinbase"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2020-01-17T00:00:00.000000000Z&paging_from=start&markets=coinbase-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2020-01-18T00:00:00.000000000Z")
mydata["binance"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2020-01-17T00:00:00.000000000Z&paging_from=start&markets=binance-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2020-01-18T00:00:00.000000000Z")


df = pd.DataFrame(mydata["binance"], columns=[ 'timestamp', 'price', 'amount', 'side', 'market'])
#df = pd.DataFrame(mydata["coinbase"], columns=[ 'timestamp', 'price', 'amount', 'side', 'market'])


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

