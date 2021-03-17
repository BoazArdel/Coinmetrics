import json
import datetime 
import matplotlib.pyplot as plt


with open('data_dump_final_cb.txt') as json_file:
    mydata = json.load(json_file)

for datagram in mydata: 
    now = datetime.datetime.strptime(datagram["timestamp"], '%Y-%m-%dT%H:%M:%S.%f000Z')
'''  
    #print(now.minute)
if now.year == 2020 and now.hour == 0 and now.minute < 5 and datagram["market"] == "bitfinex-btc-usd-spot": 
        print(datagram)
'''
if now.year == 2018 and now.hour == 0 and now.minute < 5 and datagram["market"] == "kraken-btc-usd-spot": 
        print(datagram)
if now.year == 2019 and now.hour == 0 and now.minute < 5 and datagram["market"] == "kraken-btc-usd-spot": 
        print(datagram)
'''
for obs in mydata:
    obs["time"] = datetime.datetime.strptime(obs["timestamp"], '%Y-%m-%dT%H:%M:%S.%f000Z')
    obs["seconds_since_midnight"] = obs["time"].hour * 3600 + obs["time"].minute * 60 + obs["time"].second + (obs["time"].microsecond / 1000000.0)

#plot anomaly interval
plt.plot(int(float(obs["seconds_since_midnight"])), int(float(datagram["price"])))
plt.show()
'''

