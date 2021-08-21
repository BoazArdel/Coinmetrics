####################### DATA Preparation ################
import pandas as pd


def avarage_interval_creator(data,interval):
    last_interval = 0
    temp_amount_sum = 0
    temp_price_sum = 0
    temp_time_sum = 0
    temp_pq_sum = 0
    min_price = 0
    max_price = 0

    counter = 0
    new_data = []
    last_time = ""
    market = ""

    for obs in data.iloc:
        if int(obs["seconds_since_midnight"]/interval) == int(last_interval):
            temp_amount_sum = temp_amount_sum + float(obs["amount"])
            temp_time_sum = temp_time_sum + obs["seconds_since_midnight"]
            temp_price_sum = temp_price_sum + float(obs["price"])
            temp_pq_sum = temp_pq_sum + float(obs["p*q"])
            market = obs["market"]
            last_time = obs["timestamp"]
            counter = counter + 1
            
            if counter==1:
                min_price = max_price = float(obs["price"])
            else: 
                if float(obs["price"]) <= min_price: min_price=float(obs["price"])
                if float(obs["price"]) >= max_price: max_price=float(obs["price"])

        else:
            if counter==0: counter=1 
            new_data.append({"interval_id": int(last_interval), "avg_seconds_since_midnight": temp_time_sum/counter, "avg_amount": temp_amount_sum/counter, "avg_price": temp_price_sum/counter, "min_price": min_price, "max_price": max_price ,"volume": temp_pq_sum/counter, "market": market , "year": last_time.year, "month": last_time.month, "day": last_time.day, "hour": last_time.hour,"time": last_time, "is_kraken": int("kraken" in market), "is_bitfinex": int("bitfinex" in market), "is_bitstamp": int("bitstamp" in market), "is_coinbase": int("coinbase" in market), "VWAP": temp_pq_sum/temp_amount_sum, "amount": obs["amount"], "num_trades": counter})
            
            last_interval = obs["seconds_since_midnight"]/interval
            temp_amount_sum = float(obs["amount"])
            temp_time_sum = obs["seconds_since_midnight"]
            temp_price_sum = float(obs["price"])
            temp_pq_sum = float(obs["p*q"])
            counter = 1
            last_time = obs["timestamp"]
            market = obs["market"]
            min_price = max_price = float(obs["price"])
    
    return pd.DataFrame(new_data)

def Observ_merge(data):
    new_data = []
    temp_obj = {"interval_id": "", "year": "" ,"month": "", "day": "", "hour": "", "avg_sec_bs": "", "avg_am_bs": "", "avg_pr_bs": "", "min_pr_bs": "", "max_pr_bs": "", "val_bs": "", "avg_sec_kr": "", "avg_am_kr": "", "avg_pr_kr": "", "min_pr_kr": "", "max_pr_kr": "", "val_kr": "", "avg_sec_bf": "", "avg_am_bf": "", "avg_pr_bf": "", "min_pr_bf": "", "max_pr_bf": "", "val_bf": "", "avg_sec_cb": "", "avg_am_cb": "", "avg_pr_cb": "", "min_pr_cb": "", "max_pr_cb": "", "val_cb": "", "amount_btc_bs": "", "amount_btc_bf": "", "amount_btc_cb": "", "amount_btc_kr": "", "VWAP_bs": "", "VWAP_bf": "", "VWAP_cb": "", "VWAP_kr": "", "num_trades_bs": "", "num_trades_bf": "", "num_trades_cb": "", "num_trades_kr": ""}
    last_obs = data.iloc[0]
    
    for obs in data.iloc:

        if (obs["interval_id"] == last_obs["interval_id"]) and (obs["day"] == last_obs["day"]): 
            
            if obs["is_bitfinex"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["month"] = last_obs["month"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["hour"] = last_obs["hour"]
                temp_obj["avg_sec_bf"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_bf"]= last_obs["avg_amount"]
                temp_obj["avg_pr_bf"] = last_obs["avg_price"]
                temp_obj["min_pr_bf"] = last_obs["min_price"]
                temp_obj["max_pr_bf"] = last_obs["max_price"]
                temp_obj["val_bf"] = last_obs["volume"]
                temp_obj["VWAP_bf"] = last_obs["VWAP"]
                temp_obj["amount_btc_bf"] = last_obs["amount"]
                temp_obj["num_trades_bf"] = last_obs["num_trades"]
                #temp_obj["max_VWAP"] = max(int(temp_obj["VWAP_bf"].strip() or 0),int(temp_obj["VWAP_bs"].strip() or 0),int(temp_obj[""].strip() or 0))

            elif obs["is_bitstamp"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["month"] = last_obs["month"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["hour"] = last_obs["hour"]
                temp_obj["avg_sec_bs"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_bs"]= last_obs["avg_amount"]
                temp_obj["avg_pr_bs"] = last_obs["avg_price"]
                temp_obj["min_pr_bs"] = last_obs["min_price"]
                temp_obj["max_pr_bs"] = last_obs["max_price"]
                temp_obj["val_bs"] = last_obs["volume"]
                temp_obj["VWAP_bs"] = last_obs["VWAP"]
                temp_obj["amount_btc_bs"] = last_obs["amount"]
                temp_obj["num_trades_bs"] = last_obs["num_trades"]


            elif obs["is_kraken"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["month"] = last_obs["month"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["hour"] = last_obs["hour"]
                temp_obj["avg_sec_kr"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_kr"]= last_obs["avg_amount"]
                temp_obj["avg_pr_kr"] = last_obs["avg_price"]
                temp_obj["min_pr_kr"] = last_obs["min_price"]
                temp_obj["max_pr_kr"] = last_obs["max_price"]
                temp_obj["val_kr"] = last_obs["volume"]
                temp_obj["VWAP_kr"] = last_obs["VWAP"]
                temp_obj["amount_btc_kr"] = last_obs["amount"]
                temp_obj["num_trades_kr"] = last_obs["num_trades"]



            elif obs["is_coinbase"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["month"] = last_obs["month"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["hour"] = last_obs["hour"]
                temp_obj["avg_sec_cb"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_cb"]= last_obs["avg_amount"]
                temp_obj["avg_pr_cb"] = last_obs["avg_price"]
                temp_obj["min_pr_cb"] = last_obs["min_price"]
                temp_obj["max_pr_cb"] = last_obs["max_price"]
                temp_obj["val_cb"] = last_obs["volume"]
                temp_obj["VWAP_cb"] = last_obs["VWAP"]
                temp_obj["amount_btc_cb"] = last_obs["amount"]
                temp_obj["num_trades_cb"] = last_obs["num_trades"]

            #print(last_obs["interval_id"])
            last_obs = obs    

        else:
            new_data.append(temp_obj) 
            temp_obj = {"interval_id": "", "year": "" ,"month": "", "day": "", "hour": "", "avg_sec_bs": "", "avg_am_bs": "", "avg_pr_bs": "", "min_pr_bs": "", "max_pr_bs": "", "val_bs": "", "avg_sec_kr": "", "avg_am_kr": "", "avg_pr_kr": "", "min_pr_kr": "", "max_pr_kr": "", "val_kr": "", "avg_sec_bf": "", "avg_am_bf": "", "avg_pr_bf": "", "min_pr_bf": "", "max_pr_bf": "", "val_bf": "", "avg_sec_cb": "", "avg_am_cb": "", "avg_pr_cb": "", "min_pr_cb": "", "max_pr_cb": "", "val_cb": "", "amount_btc_bs": "", "amount_btc_bf": "", "amount_btc_cb": "", "amount_btc_kr": "", "VWAP_bs": "", "VWAP_bf": "", "VWAP_cb": "", "VWAP_kr": "", "num_trades_bs": "", "num_trades_bf": "", "num_trades_cb": "", "num_trades_kr": ""}    
            
            if obs["is_bitfinex"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["month"] = last_obs["month"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["hour"] = last_obs["hour"]
                temp_obj["avg_sec_bf"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_bf"]= last_obs["avg_amount"]
                temp_obj["avg_pr_bf"] = last_obs["avg_price"]
                temp_obj["min_pr_bf"] = last_obs["min_price"]
                temp_obj["max_pr_bf"] = last_obs["max_price"]
                temp_obj["val_bf"] = last_obs["volume"]
                temp_obj["VWAP_bf"] = last_obs["VWAP"]
                temp_obj["amount_btc_bf"] = last_obs["amount"]
                temp_obj["num_trades_bf"] = last_obs["num_trades"]




            elif obs["is_bitstamp"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["month"] = last_obs["month"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["hour"] = last_obs["hour"]
                temp_obj["avg_sec_bs"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_bs"]= last_obs["avg_amount"] 
                temp_obj["avg_pr_bs"] = last_obs["avg_price"] 
                temp_obj["min_pr_bs"] = last_obs["min_price"] 
                temp_obj["max_pr_bs"] = last_obs["max_price"]
                temp_obj["val_bs"] = last_obs["volume"]
                temp_obj["VWAP_bs"] = last_obs["VWAP"]
                temp_obj["amount_btc_bs"] = last_obs["amount"]
                temp_obj["num_trades_bs"] = last_obs["num_trades"]



            elif obs["is_kraken"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["month"] = last_obs["month"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["hour"] = last_obs["hour"]
                temp_obj["avg_sec_kr"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_kr"]= last_obs["avg_amount"]
                temp_obj["avg_pr_kr"] = last_obs["avg_price"] 
                temp_obj["min_pr_kr"] = last_obs["min_price"] 
                temp_obj["max_pr_kr"] = last_obs["max_price"] 
                temp_obj["val_kr"] = last_obs["volume"]
                temp_obj["VWAP_kr"] = last_obs["VWAP"]
                temp_obj["amount_btc_kr"] = last_obs["amount"]
                temp_obj["num_trades_kr"] = last_obs["num_trades"]



            elif obs["is_coinbase"]==1:
                temp_obj["interval_id"] =  last_obs["interval_id"]
                temp_obj["year"] = last_obs["year"]
                temp_obj["month"] = last_obs["month"]
                temp_obj["day"] = last_obs["day"]
                temp_obj["hour"] = last_obs["hour"]
                temp_obj["avg_sec_cb"] = last_obs["avg_seconds_since_midnight"]
                temp_obj["avg_am_cb"]= last_obs["avg_amount"]
                temp_obj["avg_pr_cb"] = last_obs["avg_price"] 
                temp_obj["min_pr_cb"] = last_obs["min_price"] 
                temp_obj["max_pr_cb"] = last_obs["max_price"] 
                temp_obj["val_cb"] = last_obs["volume"]
                temp_obj["VWAP_cb"] = last_obs["VWAP"]
                temp_obj["amount_btc_cb"] = last_obs["amount"]
                temp_obj["num_trades_cb"] = last_obs["num_trades"]

            last_obs = obs  
    #print(new_data)
    return pd.DataFrame(new_data)