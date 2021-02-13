import json
import datetime
from os import read
from passwords import API_KEY

#local lib
import miner
import preparing
import exporter

mydata = []

start_time_date = ['2021-01-15T00:00:00.000000000Z','2020-01-17T00:00:00.000000000Z','2019-01-18T00:00:00.000000000Z','2018-01-19T00:00:00.000000000Z','2017-01-20T00:00:00.000000000Z','2016-01-22T00:00:00.000000000Z','2015-01-23T00:00:00.000000000Z']
end_time_date = ['2021-01-16T00:00:00.000000000Z','2020-01-18T00:00:00.000000000Z','2019-01-19T00:00:00.000000000Z','2018-01-20T00:00:00.000000000Z','2017-01-21T00:00:00.000000000Z','2016-01-23T00:00:00.000000000Z','2015-01-24T00:00:00.000000000Z']

for i in range(0,7):
    mydata = mydata + miner.getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date[i]+'&paging_from=start&markets=bitstamp-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date[i])
    mydata = mydata + miner.getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date[i]+'&paging_from=start&markets=kraken-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date[i])
    mydata = mydata + miner.getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date[i]+'&paging_from=start&markets=bitfinex-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date[i])
    mydata = mydata + miner.getDataByEndDate('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time='+start_time_date[i]+'&paging_from=start&markets=coinbase-btc-usd-spot&pretty=true&api_key=' + API_KEY,end_time_date[i])

with open('data_dump_final_cb.txt', 'w') as outfile:
    json.dump(mydata, outfile)

with open('data_dump_final_cb.txt') as json_file:
    mydata = json.load(json_file)

#adding parameters
for obs in mydata:
    obs["time"] = datetime.datetime.strptime(obs["timestamp"], '%Y-%m-%dT%H:%M:%S.%f000Z')
    obs["seconds_since_midnight"] = obs["time"].hour * 3600 + obs["time"].minute * 60 + obs["time"].second + (obs["time"].microsecond / 1000000.0)

interval = 600 #10 min interval, in seconds

mydata = preparing.avarage_interval_creator(mydata,interval)
mydata = sorted(mydata,key=(lambda s: s['time']))
mydata = preparing.Observ_merge(mydata,interval)


with open('data6.txt', 'w') as outfile:
    json.dump(mydata, outfile, indent=4, sort_keys=True, default=str)

exporter.export_to_excel(mydata,["interval_id", "year", "day", "avg_sec_bs", "avg_am_bs", "avg_pr_bs", "min_pr_bs", "max_pr_bs", "val_bs", "avg_sec_kr", "avg_am_kr", "avg_pr_kr", "min_pr_kr", "max_pr_kr", "val_kr", "avg_sec_bf", "avg_am_bf", "avg_pr_bf", "min_pr_bf", "max_pr_bf", "val_bf", "avg_sec_cb", "avg_am_cb", "avg_pr_cb", "min_pr_cb", "max_pr_cb", "val_cb"])
#exporter.xslx_to_dta(input("without suffix, your excel name:"))