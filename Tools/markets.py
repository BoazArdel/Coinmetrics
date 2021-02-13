import requests
import json
import pprint
import pandas as pd
#import xlsxwriter
#import xlwt
from websocket import create_connection

#response = requests.get("https://api.coinmetrics.io/v2/asset_info",params={"subset":"btc,eth","exchanges":"binance"}, headers={'Authorization': '5HhxV46Nk6gJrX95837t'})
#response = requests.get("https://api.coinmetrics.io/v2/assets/eth/referencerates",params={"start":"2020-01-20","end":"2020-01-21","limit":1000,"close_type":"hourly"}, headers={'Authorization': '5HhxV46Nk6gJrX95837t'})

response = requests.get('https://api.coinmetrics.io/v4/timeseries/asset-metrics?assets=btc&metrics=PriceUSD,FlowInGEMUSD&frequency=1b&pretty=true&api_key=5HhxV46Nk6gJrX95837t').json()
print(response)
response = requests.get('https://api.coinmetrics.io/v4/catalog/assets?pretty=true&api_key=5HhxV46Nk6gJrX95837t').json()
print(response)

'''
ws = create_connection("wss://feed.coinmetrics.io/v2/trades",params={"markets":"coinbase-btc-usd-spot"},headers={'Authorization': '5HhxV46Nk6gJrX95837t'})
ws.send(json.dumps({"markets":"coinbase-btc-usd-spot"}))
result =  ws.recv()
print (result)
ws.close()
'''
#json_text = response.content
#pprint.pprint(json_text)
##df = pd.read_json(json_text)
##df.to_excel('output.xls', index=False)