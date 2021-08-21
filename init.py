import os
from subprocess import check_output

#start_time_date, end_time_date = date_iterator.date_func("2017-01-01T00:00:00.000000000Z","2021-04-01T00:00:00.000000000Z")
start_time_date = ["2017-01-01T00:00:00.000000000Z","2017-06-02T00:00:00.000000000Z", "2018-01-02T00:00:00.000000000Z","2018-06-02T00:00:00.000000000Z", "2019-01-02T00:00:00.000000000Z","2019-06-02T00:00:00.000000000Z", "2020-01-02T00:00:00.000000000Z","2020-06-02T00:00:00.000000000Z", "2021-01-02T00:00:00.000000000Z"] 
end_time_date = ["2017-06-01T00:00:00.000000000Z", "2018-01-01T00:00:00.000000000Z", "2018-06-01T00:00:00.000000000Z","2019-01-01T00:00:00.000000000Z", "2019-06-01T00:00:00.000000000Z", "2020-01-01T00:00:00.000000000Z", "2020-06-01T00:00:00.000000000Z", "2021-01-01T00:00:00.000000000Z", "2021-06-01T00:00:00.000000000Z"] 
#markets = ["bitstamp","kraken","bitfinex","coinbase"]
#print(check_output("python3 C:\\Users\\GabrielaA\\Documents\\GitHub\\Coinmetrics\\main.py kraken "+ "2020-01-02T00:00:00.000000000Z" +" "+"2020-06-01T00:00:00.000000000Z", shell=True).decode())
#print(check_output("python3 C:\\Users\\GabrielaA\\Documents\\GitHub\\Coinmetrics\\main.py kraken "+ "2020-06-02T00:00:00.000000000Z" +" "+ "2021-01-01T00:00:00.000000000Z", shell=True).decode())
#print(check_output("python3 C:\\Users\\GabrielaA\\Documents\\GitHub\\Coinmetrics\\main.py kraken "+ "2021-01-02T00:00:00.000000000Z"+" "+"2021-06-01T00:00:00.000000000Z", shell=True).decode())
markets = ["coinbase"]
for market in markets:
    for i in range(0, len(start_time_date)):
       print(check_output("python3 C:\\Users\\GabrielaA\\Documents\\GitHub\\Coinmetrics\\main.py "+market+" "+start_time_date[i]+" "+end_time_date[i], shell=True).decode())

#python3 C:\\Users\\GabrielaA\\Documents\\GitHub\\Coinmetrics\\main.py coinbase 2017-01-01T00:00:00.000000000Z 2017-06-02T00:00:00.000000000