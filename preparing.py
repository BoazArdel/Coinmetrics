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