import requests
import json
#from coinmetrics.api_client import CoinMetricsClient
#from coinmetrics.constants import PagingFrom
import collections
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from passwords import API_KEY

#client = CoinMetricsClient(API_KEY)


#response = requests.get('https://api.coinmetrics.io/v4/catalog-all/exchanges?pretty=true&api_key=' + API_KEY).json()
#response = requests.get('https://api.coinmetrics.io/v4/catalog-all/markets?pretty=true&api_key=' + API_KEY).json()
#response = requests.get('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2010-07-17&paging_from=start&markets=bitfinex-btc-usd-spot&pretty=true&api_key=' + API_KEY).json()
#print(response)
#exit()

#indexes request: 'mt.gox-btc-usd-spot'], 'min_time': '2010-07-17T23:09:17.000000000Z', 'max_time': '2014-02-25T01:59:06.000000000Z'}

#####creates json of time, amount and price per trade for a specific market in an exchange
mydata = {"gox" : [], "finex" : []}

def getDataByEndDate(url,date):
    data = []
    response = requests.get(url).json()
    for i in range(0,10000):   #by dates
        if(response["data"][0]["time"].split("T",1)[0]>date): break
        #print(json.dumps(response, indent=4, sort_keys=True))
        for datagram in response["data"]:
            data.append({"timestamp" : datagram["time"], "amount" : datagram["amount"], "price" : datagram["price"]})
        response = requests.get(response["next_page_url"]).json()
        print(str(i) + ":" + str(response["data"][0]["time"]))
    #print(json.dumps(data, indent=4, sort_keys=True))
    return data


mydata["gox"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2013-07-17&paging_from=start&markets=mt.gox-btc-usd-spot&pretty=true&api_key='+ API_KEY,"2013-07-20")
mydata["finex"] = getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2013-07-17&paging_from=start&markets=bitfinex-btc-usd-spot&pretty=true&api_key=' + API_KEY,"2013-07-20")

with open('data.txt', 'w') as outfile:
    json.dump(mydata, outfile)




with open('data.txt') as json_file:
    mydata = json.load(json_file)

#####counter of how many instances (trades) were every day
for market in ["gox","finex"]:
    num_of_trades = []
    for trade in mydata[market]:
        num_of_trades.append(trade["timestamp"].split("T",1)[0])
    #####plot of frequency of trades per day
    w = collections.Counter(num_of_trades)
    plt.plot(list(w.keys()), list(w.values()))

plt.legend(["gox", "finex"])
plt.show()

with open('data.txt') as json_file:
    mydata = json.load(json_file)

for market in ["gox","finex"]:
    rate_of_price = []
    time_of_price = []
    last_rate = float(0)
    last_time=""
    for trade in mydata[market]:
        if((float(trade["price"]) != last_rate) and (last_time<trade["timestamp"]) ):
            rate_of_price.append(trade["price"])
            time_of_price.append(trade["timestamp"])
            last_rate = float(trade["price"])
            last_time = trade["timestamp"]
    print(len(time_of_price),len(rate_of_price))
    print(time_of_price[:100])
    if(market == "gox"):
        plt.plot(time_of_price[:1000], rate_of_price[:1000])
    else:
        plt.plot(time_of_price[:100], rate_of_price[:100])
        plt.gca().invert_yaxis()


plt.legend(["gox", "finex"])
plt.show()