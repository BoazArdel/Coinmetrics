#current price plot creator
'''
workflow:
#connect to API
#collect list of all markets
#choose btc-usd markets
for each market, collect current BTC-USD price
plot dots: y price x market
'''
import datetime
import requests
import json 
#local libs
from passwords import API_KEY
'''
#current prices- not working!
now_init = format(datetime.datetime.now())
#print ('Current date/time: {}'.format(datetime.datetime.now()))
now_str = datetime.datetime.strptime(now_init, '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%dT%H:%M:%SZ')

start_time = now_str 
print(start_time)
'''
markets = []

response = requests.get('https://api.coinmetrics.io/v4/catalog-all/markets?pretty=true&api_key=' + API_KEY).json()
'''
print(response)

#save json from API
with open('Data/markets_list.txt', 'w') as json_file:
    json.dump(response, json_file, indent=4, sort_keys=True, default=str)
print("file created")

#load json from file 

with open('Data/markets_list.txt') as json_file:
    markets = json.load(json_file)
'''

for obs in response["data"]:
    if "-btc-" in obs["market"] and "-usd-" in obs["market"]:
        markets.append(obs["market"])

def last_price(markets):   
    prices = [] 
    #outfile = open('Data/last_prices'+now+'.txt', 'w')

    for market in markets:
        #response2 = requests.get('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=' + start_time+ '&paging_from=start&markets=' + market + '&pretty=true&api_key=' + API_KEY).json()
        response2 = requests.get('https://api.coinmetrics.io/v4/timeseries/market-trades?start_time=2021-05-21T23:00:00.000000000Z&paging_from=start&markets=' + market + '&pretty=true&api_key=' + API_KEY).json()
        
    for datagram in response2["data"]:
        obs = {"timestamp": datagram["time"], "amount": datagram["amount"], "price": datagram["price"], "market": datagram["market"]}
        prices.append(obs) 

    return prices


print(last_price(markets))

print("done")

    
