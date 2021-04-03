import requests
import json
from passwords import API_KEY
import datetime

########## API extractor ###############
def getDataByEndDate(url,selected_date,output_file):
    
    data = []
    response = requests.get(url).json()
    for i in range(0,10000): 
        if(response["data"][0]["time"]>selected_date): break
        #print(json.dumps(response, indent=4, sort_keys=True)) <if DEBUG>
        
        for datagram in response["data"]:
                obs = {"timestamp": datagram["time"], "amount": datagram["amount"], "price": datagram["price"], "market": datagram["market"]}
                data.append(obs) #to add 'side'
                output_file.write(str(obs))
        response = requests.get(response["next_page_url"]).json()
        print(str(i) + ":" + str(response["data"][0]["time"]))

    #print(json.dumps(data, indent=4, sort_keys=True))
    return data