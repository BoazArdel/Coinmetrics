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
from passwords import API_KEY

def exportExcel():
    global df

    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel(export_file_path, index=False, header=True)


saveAsButtonExcel = tk.Button(text='Export Excel', command=exportExcel, bg='green', fg='white',
                              font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButtonExcel)

root.mainloop()

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


mydata = {"kraken" : [], "finex" : [], "bitstamp" : []}
selected_date = "2020-07-17T20:00:00.000000000Z"
def getDataByEndDate(url,selected_date):
    data = []
    response = requests.get(url).json()
    for i in range(0,10000):   #by dates
        if(response["data"][0]["time"]>selected_date): break
        #print(json.dumps(response, indent=4, sort_keys=True))
        for datagram in response["data"]:
                data.append({"timestamp" : datetime.datetime.strptime(datagram["time"], '%Y-%m-%dT%H:%M:%S.%f000Z'), "amount" : datagram["amount"], "price" : datagram["price"]})
        response = requests.get(response["next_page_url"]).json()
        print(str(i) + ":" + str(response["data"][0]["time"]))
    #print(json.dumps(data, indent=4, sort_keys=True))
    return data

mydata["kraken"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2020-07-17T20:00:00.000000000Z&paging_from=start&markets=kraken-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2020-07-17T21:00:00.000000000Z")
mydata["finex"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2020-07-17T20:00:00.000000000Z&paging_from=start&markets=bitfinex-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2020-07-17T21:00:00.000000000Z")
mydata["bitstamp"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2020-07-17T20:00:00.000000000Z&paging_from=start&markets=bitstamp-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2020-07-17T21:00:00.000000000Z")

#with open('data2.txt', 'w') as outfile:
#    json.dump(mydata, outfile, cls=DateTimeEncoder)



#####counter of how many instances (trades) were every day
for market in ["kraken","finex","bitstamp"]:
    num_of_trades = []
    dates = []
    for trade in mydata[market]:
        num_of_trades.append(str(trade["timestamp"]).split(":")[0]+str(trade["timestamp"]).split(":")[1])
        dates.append(trade["timestamp"])
    #####plot of frequency of trades per day
    w = collections.Counter(num_of_trades)
    plt.plot(list(w.keys()), list(w.values()))

plt.legend(["kraken","finex","bitstamp"])
plt.title('frequency of trades per day')
plt.show()

#with open('data2.txt') as json_file:
#    mydata = json.load(json_file, cls=DateTimeEncoder)
'''
fig, ax = plt.subplots() # using matplotlib's Object Oriented API
for market in ["kraken","finex","bitstamp"]:
    rate_of_price = []
    time_of_price = []
    last_rate = float(0)
    last_time=""
    for trade in mydata[market]:
        rate_of_price.append(float(trade["price"]))
        time_of_price.append(trade["timestamp"])
        last_rate = float(trade["price"])
        last_time = trade["timestamp"]
    plt.plot(time_of_price,rate_of_price)
    plt.title('Graph of prices over an hour, starting from' + selected_date)
    plt.xlabel('Time')
    plt.ylabel('Price')
    #sorted_price = [rate_of_price for _, rate_of_price in sorted(zip(mdates.date2num(time_of_price), rate_of_price))]
    #sorted_time = mdates.date2num(sorted(time_of_price))
    #ax.plot_date(sorted_time,sorted_price, 'k-')
    #hfmt = mdates.DateFormatter('%H:%M:%S') #"2013-07-17T00:10:01.000000000Z"
    #ax.xaxis.set_major_formatter(hfmt)
    #plt.gcf().autofmt_xdate()

    #plt.plot (Z)
ax.legend(["kraken","finex","bitstamp"])
plt.show()
'''