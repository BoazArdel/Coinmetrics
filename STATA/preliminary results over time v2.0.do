use "C:\Users\boaza\Downloads\15to20.dta"
*use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta"

***preliminary results do file***
rename min_price price_min
rename max_price price_max

gen kr_diff = price_max - price_min if is_kraken == 1
gen bf_diff = price_max - price_min if is_bitfinex == 1
gen bs_diff = price_max - price_min if is_bitstamp == 1

gen kr_price_mean = avg_price if is_kraken ==1
gen bf_price_mean = avg_price if is_bitfinex ==1
gen bs_price_mean = avg_price if is_bitstamp ==1

gen bf_kr = bf_price_mean - kr_price_mean
gen bf_bs = bf_price_mean - bs_price_mean
gen kr_bs = kr_price_mean - bs_price_mean

***summary stats***
sum bf_price_mean bs_price_mean kr_price_mean if year == 2015
sum bf_price_mean bs_price_mean kr_price_mean if year == 2016
sum bf_price_mean bs_price_mean kr_price_mean if year == 2017
sum bf_price_mean bs_price_mean kr_price_mean if year == 2018
sum bf_price_mean bs_price_mean kr_price_mean if year == 2019
sum bf_price_mean bs_price_mean kr_price_mean if year == 2020

***for year 2015***

correl *_price_mean if year == 2015
correl *price_min if year == 2015
correl *price_max if year == 2015
correl bf_kr *price_mean value if year == 2015

***for year 2016***

correl *price_mean if year == 2016
correl *price_min if year == 2016
correl *price_max if year == 2016
correl bf_kr *price_mean value if year == 2016

***for year 2017***

correl *price_mean if year == 2017
correl *price_min if year == 2017
correl *price_max if year == 2017
*correl bf_kr *price_mean value if year == 2017

***for year 2018***

correl *price_mean if year == 2018
correl *price_min if year == 2018
correl *price_max if year == 2018
correl bf_kr *price_mean value if year == 2018

***for year 2019***

correl *price_mean if year == 2019
correl *price_min if year == 2019
correl *price_max if year == 2019
correl bf_kr *price_mean value if year == 2019

***for year 2020***

correl *price_mean if year == 2020
correl *price_min if year == 2020
correl *price_max if year == 2020
correl bf_kr *price_mean value if year == 2020

***Correlation between range within an exchange and trade in that exchange***

sum kr_diff bf_diff bs_diff if year ==2015
sum kr_diff bf_diff bs_diff if year ==2016
sum kr_diff bf_diff bs_diff if year ==2017
sum kr_diff bf_diff bs_diff if year ==2018
sum kr_diff bf_diff bs_diff if year ==2019
sum kr_diff bf_diff bs_diff if year ==2020

correl kr_diff bf_diff bs_diff value if year==2015 
correl kr_diff bf_diff bs_diff value if year==2016
correl kr_diff bf_diff bs_diff value if year==2017
correl kr_diff bf_diff bs_diff value if year==2018
correl kr_diff bf_diff bs_diff value if year==2019
correl kr_diff bf_diff bs_diff value if year==2020 

***look at one exchange's minimum price versus another exchange's maximum price***
***kr and bf***
gen spread_kr_bf = kr_price_max - bf_price_min
gen spread_bf_kr = bf_price_max - kr_price_min
***kr and bs***
gen spread_kr_bs = kr_price_max - bs_price_min
gen spread_bs_kr = bs_price_max - kr_price_min
***bs and bf***
gen spread_bs_bf = bs_price_max - bf_price_min
gen spread_bf_bs = bf_price_max - bs_price_min

sum spread* if year == 2015
sum spread* if year == 2016
sum spread* if year == 2017
sum spread* if year == 2018
sum spread* if year == 2019
sum spread* if year == 2020




