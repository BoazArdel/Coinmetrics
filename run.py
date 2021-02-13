### changes, including: 2015-2021; coinbase, kraken, bitfinex, bitstamp

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
'''
########## API extractor ###############
def getDataByEndDate(url,selected_date):
    data = []
    response = requests.get(url).json()
    for i in range(0,10000): 
        if(response["data"][0]["time"]>selected_date): break
        #print(json.dumps(response, indent=4, sort_keys=True)) <if DEBUG>
        
        for datagram in response["data"]:
                data.append({"timestamp": datagram["time"], "amount": datagram["amount"], "price": datagram["price"], "market": datagram["market"]}) #to add 'side'
        
        response = requests.get(response["next_page_url"]).json()
        print(str(i) + ":" + str(response["data"][0]["time"]))

    #print(json.dumps(data, indent=4, sort_keys=True))
    return data

#################

mydata = []

start_time_date = ['2021-01-15T00:00:00.000000000Z','2020-01-17T00:00:00.000000000Z','2019-01-18T00:00:00.000000000Z','2018-01-19T00:00:00.000000000Z','2017-01-20T00:00:00.000000000Z','2016-01-22T00:00:00.000000000Z','2015-01-23T00:00:00.000000000Z']
end_time_date = ['2021-01-16T00:00:00.000000000Z','2020-01-18T00:00:00.000000000Z','2019-01-19T00:00:00.000000000Z','2018-01-20T00:00:00.000000000Z','2017-01-21T00:00:00.000000000Z','2016-01-23T00:00:00.000000000Z','2015-01-24T00:00:00.000000000Z']

for i in range(0,7):
    mydata = mydata + getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date[i]+'&paging_from=start&markets=bitstamp-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date[i])
    mydata = mydata + getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date[i]+'&paging_from=start&markets=kraken-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date[i])
    mydata = mydata + getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date[i]+'&paging_from=start&markets=bitfinex-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date[i])
    mydata = mydata + getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date[i]+'&paging_from=start&markets=coinbase-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date[i])



with open('data_dump_final_cb.txt', 'w') as outfile:
    json.dump(mydata, outfile)
'''
with open('data_dump_final_cb.txt') as json_file:
    mydata = json.load(json_file)

####################### DATA Preparation ################

def avarage_interval_creator(data,interval):
    last_interval = 0
    temp_amount_sum = 0
    temp_price_sum = 0
    temp_time_sum = 0
    min_price = 0
    max_price = 0
    counter = 0
    new_data = []
    last_time = None
    market = None

    for obs in data:
        if int(obs["seconds_since_midnight"]/interval) == int(last_interval):
            temp_amount_sum = temp_amount_sum + float(obs["amount"])
            temp_time_sum = temp_time_sum + obs["seconds_since_midnight"]
            temp_price_sum = temp_price_sum + float(obs["price"])
            market = obs["market"]
            last_time = obs["time"]
            counter = counter + 1
            
            if counter==1:
                min_price = max_price = float(obs["price"])
            else: 
                if float(obs["price"]) <= min_price: min_price=float(obs["price"])
                if float(obs["price"]) >= max_price: max_price=float(obs["price"])

        else:
            if counter==0: counter=1 
            new_data.append({"interval_id": int(last_interval), "avg_seconds_since_midnight": temp_time_sum/counter, "avg_amount": temp_amount_sum/counter, "avg_price": temp_price_sum/counter, "min_price": min_price, "max_price": max_price ,"value": (temp_amount_sum/counter)*(temp_price_sum/counter), "market": market , "year": last_time.year, "day": last_time.day,"time": last_time, "is_kraken": int("kraken" in market), "is_bitfinex": int("bitfinex" in market), "is_bitstamp": int("bitstamp" in market), "is_coinbase": int("coinbase" in market)})
            
            last_interval = obs["seconds_since_midnight"]/interval
            temp_amount_sum = float(obs["amount"])
            temp_time_sum = obs["seconds_since_midnight"]
            temp_price_sum = float(obs["price"])
            counter = 1
            last_time = obs["time"]
            market = obs["market"]
            min_price = max_price = float(obs["price"])
    
    return new_data

def Observ_merge(data,interval):
    new_data = []
    temp_obj = {"interval_id": None, "year": None ,"day": None, "avg_sec_bs": None, "avg_am_bs": None, "avg_pr_bs": None, "min_pr_bs": None, "max_pr_bs": None, "val_bs": None, "avg_sec_kr": None, "avg_am_kr": None, "avg_pr_kr": None, "min_pr_kr": None, "max_pr_kr": None, "val_kr": None, "avg_sec_bf": None, "avg_am_bf": None, "avg_pr_bf": None, "min_pr_bf": None, "max_pr_bf": None, "val_bf": None, "avg_sec_cb": None, "avg_am_cb": None, "avg_pr_cb": None, "min_pr_cb": None, "max_pr_cb": None, "val_cb": None}
    last_obs = data[0]

    for obs in data:
        if (obs["interval_id"] == last_obs["interval_id"]) and (obs["day"] == last_obs["day"]): 
            
            if obs["is_bitfinex"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["avg_sec_bf"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_bf"]= last_obs["avg_amount"]
                temp_obj["avg_pr_bf"] = last_obs["avg_price"]
                temp_obj["min_pr_bf"] = last_obs["min_price"]
                temp_obj["max_pr_bf"] = last_obs["max_price"]
                temp_obj["val_bf"] = last_obs["value"]
            elif obs["is_bitstamp"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["avg_sec_bs"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_bs"]= last_obs["avg_amount"]
                temp_obj["avg_pr_bs"] = last_obs["avg_price"]
                temp_obj["min_pr_bs"] = last_obs["min_price"]
                temp_obj["max_pr_bs"] = last_obs["max_price"]
                temp_obj["val_bs"] = last_obs["value"]
            elif obs["is_kraken"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["avg_sec_kr"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_kr"]= last_obs["avg_amount"]
                temp_obj["avg_pr_kr"] = last_obs["avg_price"]
                temp_obj["min_pr_kr"] = last_obs["min_price"]
                temp_obj["max_pr_kr"] = last_obs["max_price"]
                temp_obj["val_kr"] = last_obs["value"]
            elif obs["is_coinbase"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["avg_sec_cb"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_cb"]= last_obs["avg_amount"]
                temp_obj["avg_pr_cb"] = last_obs["avg_price"]
                temp_obj["min_pr_cb"] = last_obs["min_price"]
                temp_obj["max_pr_cb"] = last_obs["max_price"]
                temp_obj["val_cb"] = last_obs["value"]
            last_obs = obs    

        else:
            new_data.append(temp_obj) 
            temp_obj = {"interval_id": None, "year": None ,"day": None, "avg_sec_bs": None, "avg_am_bs": None, "avg_pr_bs": None, "min_pr_bs": None, "max_pr_bs": None, "val_bs": None, "avg_sec_kr": None, "avg_am_kr": None, "avg_pr_kr": None, "min_pr_kr": None, "max_pr_kr": None, "val_kr": None, "avg_sec_bf": None, "avg_am_bf": None, "avg_pr_bf": None, "min_pr_bf": None, "max_pr_bf": None, "val_bf": None, "avg_sec_cb": None, "avg_am_cb": None, "avg_pr_cb": None, "min_pr_cb": None, "max_pr_cb": None, "val_cb": None}    
            
            if obs["is_bitfinex"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["avg_sec_bf"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_bf"]= last_obs["avg_amount"]
                temp_obj["avg_pr_bf"] = last_obs["avg_price"]
                temp_obj["min_pr_bf"] = last_obs["min_price"]
                temp_obj["max_pr_bf"] = last_obs["max_price"]
                temp_obj["val_bf"] = last_obs["value"]
            elif obs["is_bitstamp"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["avg_sec_bs"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_bs"]= last_obs["avg_amount"] 
                temp_obj["avg_pr_bs"] = last_obs["avg_price"] 
                temp_obj["min_pr_bs"] = last_obs["min_price"] 
                temp_obj["max_pr_bs"] = last_obs["max_price"]
                temp_obj["val_bs"] = last_obs["value"]
            elif obs["is_kraken"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["avg_sec_kr"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_kr"]= last_obs["avg_amount"]
                temp_obj["avg_pr_kr"] = last_obs["avg_price"] 
                temp_obj["min_pr_kr"] = last_obs["min_price"] 
                temp_obj["max_pr_kr"] = last_obs["max_price"] 
                temp_obj["val_kr"] = last_obs["value"]
            elif obs["is_coinbase"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["avg_sec_cb"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_cb"]= last_obs["avg_amount"]
                temp_obj["avg_pr_cb"] = last_obs["avg_price"] 
                temp_obj["min_pr_cb"] = last_obs["min_price"] 
                temp_obj["max_pr_cb"] = last_obs["max_price"] 
                temp_obj["val_cb"] = last_obs["value"]
            last_obs = obs    
  
    return new_data    



#adding parameters
#for obs in mydata:
#    obs["time"] = datetime.datetime.strptime(obs["timestamp"], '%Y-%m-%dT%H:%M:%S.%f000Z')
#    obs["seconds_since_midnight"] = obs["time"].hour * 3600 + obs["time"].minute * 60 + obs["time"].second + (obs["time"].microsecond / 1000000.0)

#interval = 600 #10 min interval, in seconds
#interval = 60 #1 min interval, in seconds
for obs in mydata:
    obs["time"] = datetime.datetime.strptime(obs["timestamp"], '%Y-%m-%dT%H:%M:%S.%f000Z')
    obs["seconds_since_midnight"] = obs["time"].hour * 3600 + obs["time"].minute * 60 + obs["time"].second + (obs["time"].microsecond / 1000000.0)


interval = 1 #1 sec interval

new_mydata = avarage_interval_creator(mydata,interval)
new_mydata = sorted(new_mydata,key=(lambda s: s['time']))

new_mydata = Observ_merge(new_mydata,interval)


################ Excel #################

df = pd.DataFrame(new_mydata, columns=["interval_id", "year", "day", "avg_sec_bs", "avg_am_bs", "avg_pr_bs", "min_pr_bs", "max_pr_bs", "val_bs", "avg_sec_kr", "avg_am_kr", "avg_pr_kr", "min_pr_kr", "max_pr_kr", "val_kr", "avg_sec_bf", "avg_am_bf", "avg_pr_bf", "min_pr_bf", "max_pr_bf", "val_bf", "avg_sec_cb", "avg_am_cb", "avg_pr_cb", "min_pr_cb", "max_pr_cb", "val_cb"])

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


with open('data6.txt', 'w') as outfile:
    json.dump(new_mydata, outfile, indent=4, sort_keys=True, default=str)