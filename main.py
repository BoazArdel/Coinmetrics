import json
import datetime,time
from passwords import API_KEY
import sys,os
import glob
import pandas as pd
import vaex
import numpy as np
import matplotlib.pyplot as plt

#local lib
import miner
import preparing

#Defines
MINING = False
PREPARE = True
#Args
market = "coinbase"
start_time_date = "2017-01-01T00:00:00.000000000Z"
end_time_date = "2017-06-02T00:00:00.000000000Z"

if len(sys.argv)==4:
    market = sys.argv[1]
    start_time_date = sys.argv[2]
    end_time_date = sys.argv[3]


if MINING==True:
    mydata = []
    now = str(datetime.datetime.now())
    print("starting run" + now)

    dumpfile = open('Data/data_dump_monthly_'+now.replace(":","")+market+start_time_date.replace(":","")+end_time_date.replace(":","")+'.txt', 'w')
    outfile = open('Data/data_incremental_monthly_'+now.replace(":","")+market+start_time_date.replace(":","")+end_time_date.replace(":","")+'.txt', 'w')
    #start_time_date, end_time_date = date_iterator.date_func("2017-01-01T00:00:00.000000000Z","2021-04-01T00:00:00.000000000Z")
    
    if market == "bitstamp":
        mydata = mydata + miner.getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date+'&paging_from=start&markets=bitstamp-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date,outfile)
    elif market == "kraken":
        mydata = mydata + miner.getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date+'&paging_from=start&markets=kraken-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date,outfile)
    elif market == "bitfinex":
        mydata = mydata + miner.getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date+'&paging_from=start&markets=bitfinex-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date,outfile)
    elif market == "coinbase":
        mydata = mydata + miner.getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date+'&paging_from=start&markets=coinbase-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date,outfile)

    json.dump(mydata, dumpfile)

if PREPARE == True:
    #open multiple files:
    mydata = pd.DataFrame()
    pd.options.mode.chained_assignment = None  # default='warn'
    mypath = os.getcwd() + '/Data'
    #mypath = "/Users/gabriela/Google Drive/Projects/GitHub/Coinmetrics/Data"
    #mypath = "/Users/GabrielaA/Documents/GitHub/Coinmetrics/Data"
    
    data_files = glob.glob(os.path.join(mypath, 'data_dump_monthly.json'))

    for file in glob.glob(os.path.join(mypath, 'data_dump_monthly_*.txt')):
        mydata = pd.concat([mydata,vaex.from_json(file).to_pandas_df()])
        print("100% negga!")

    #mydata = mydata.head(100)

    #adding parameters
    mydata["seconds_since_midnight"] = ""
    mydata["p*q"] = ""

    mydata["seconds_since_midnight"] = (mydata["timestamp"].dt.hour * 3600 + mydata["timestamp"].dt.minute * 60 + mydata["timestamp"].dt.second + (mydata["timestamp"].dt.microsecond / 1000000.0))
    mydata["p*q"] = mydata["amount"] * mydata["price"]

    interval = 600 #10 min interval, in seconds
    #print(mydata)
    
    mydata = preparing.avarage_interval_creator(mydata,interval)
    #print(mydata)
    mydata = mydata.sort_values(by=['time'])
    #print(mydata)
    #mydata = sorted(mydata,key=(lambda s: s['time']))
    mydata = preparing.Observ_merge(mydata)
    print(mydata)

    #mydata = preparing.non_interval_calculations(mydata)

    #with open('Data/prepared_data_'+now+'.txt', 'w') as outfile:
    #    json.dump(mydata, outfile, indent=4, sort_keys=True, default=str)

    mydata.to_pickle("pickle.pick")
    mydata.to_stata('final.dta') 
    #mydata=mydata.applymap(str)
    #mydata.to_stata('myfile.dta', version=117, convert_strl = mydata.columns[mydata.isnull().all()].tolist())
    
    #exporter.export_to_excel(mydata,["interval_id", "year", "month", "day", "avg_sec_bs", "avg_am_bs", "avg_pr_bs", "min_pr_bs", "max_pr_bs", "val_bs", "avg_sec_kr", "avg_am_kr", "avg_pr_kr", "min_pr_kr", "max_pr_kr", "val_kr", "avg_sec_bf", "avg_am_bf", "avg_pr_bf", "min_pr_bf", "max_pr_bf", "val_bf", "avg_sec_cb", "avg_am_cb", "avg_pr_cb", "min_pr_cb", "max_pr_cb", "val_cb", "VWAP_bs", "VWAP_bf", "VWAP_cb", "VWAP_kr","amount_btc_bs", "amount_btc_bf", "amount_btc_cb", "amount_btc_kr", "num_trades_bs", "num_trades_bf", "num_trades_cb", "num_trades_kr", "max_VWAP", "min_VWAP", "arbitrage_index"])
    #exporter.xlsx_to_dta(input("without suffix, your excel name:"))
