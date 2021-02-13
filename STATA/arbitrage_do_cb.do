**arbitrage do file: cb kr bs bf 2015-2021
set more off 


use 15to20_new_format.dta   


* ---------------------------------------------------------------* 
* ---------------------------Notation ---------------------------* 

* bs will be abbreviation of bitstamp * 
* bf will be abbreviation of bitfinex * 
* kr will be abbreviation of kraken * 
* cb will be abbreviation of coinbase * 

* bs_kr = avg_pr_bs  - avg_pr_kr  * 
* ----------------------------------------------------------------* 

* ----------------------------------------------------------------* 
* generating % differences max-min within exchange  * 
* ----------------------------------------------------------------* 


gen kr_diff = (max_pr_kr - min_pr_kr)/avg_pr_kr*100 
gen bs_diff = (max_pr_bs - min_pr_bs)/avg_pr_bs*100 
gen bf_diff = (max_pr_bf - min_pr_bf)/avg_pr_bf*100 
gen cb_diff = (max_pr_cb - min_pr_cb)/avg_pr_cb*100 


* ----------------------------------------------------------------* 
* generating % differences between exchanges  * 
* ----------------------------------------------------------------* 


gen bs_kr_diff = (avg_pr_bs  - avg_pr_kr)/avg_pr_kr*100 
gen kr_bs_diff = (avg_pr_kr  - avg_pr_bs)/avg_pr_bs*100 

gen bf_kr_diff = (avg_pr_bf  - avg_pr_kr)/avg_pr_kr*100 
gen kr_bf_diff = (avg_pr_kr  - avg_pr_bf)/avg_pr_bf*100 

gen bs_bf_diff = (avg_pr_bs  - avg_pr_bf)/avg_pr_bf*100 
gen bf_bs_diff = (avg_pr_bf  - avg_pr_bs)/avg_pr_bs*100 

gen bf_cb_diff = (avg_pr_bf  - avg_pr_cb)/avg_pr_cb*100 
gen cb_bf_diff = (avg_pr_cb  - avg_pr_bf)/avg_pr_bf*100 

gen cb_kr_diff = (avg_pr_cb  - avg_pr_kr)/avg_pr_kr*100 
gen kr_cb_diff = (avg_pr_kr  - avg_pr_cb)/avg_pr_cb*100 

gen cb_bs_diff = (avg_pr_cb  - avg_pr_bs)/avg_pr_bs*100 
gen bs_cb_diff = (avg_pr_bs  - avg_pr_cb)/avg_pr_cb*100 

* ----------------------------------------------------------------* 
* generating % differences in max-min across exchanges * 
* ----------------------------------------------------------------* 


gen bs_max_kr_min =  (max_pr_bs - min_pr_kr)/min_pr_kr*100 
gen bf_max_kr_min =  (max_pr_bf - min_pr_kr)/min_pr_kr*100 
gen bs_max_bf_min =  (max_pr_bs - min_pr_bf)/min_pr_bf*100 

gen kr_max_bs_min =  (max_pr_kr - min_pr_bs)/min_pr_bs*100 
gen kr_max_bf_min =  (max_pr_kr - min_pr_bf)/min_pr_bf*100 
gen bf_max_bs_min =  (max_pr_bf - min_pr_bs)/min_pr_bs*100 

gen bf_max_cb_min =  (max_pr_bf - min_pr_cb)/min_pr_cb*100 
gen cb_max_bf_min =  (max_pr_cb - min_pr_bf)/min_pr_bf*100 
gen bs_max_cb_min =  (max_pr_bs - min_pr_cb)/min_pr_cb*100 
gen cb_max_bs_min =  (max_pr_cb - min_pr_bs)/min_pr_bs*100 
gen kr_max_cb_min =  (max_pr_kr - min_pr_cb)/min_pr_cb*100 
gen cb_max_kr_min =  (max_pr_cb - min_pr_kr)/min_pr_kr*100 


* ---------------------------------------------------------------* 
* Corelations in Prices * 
* ---------------------------------------------------------------* 


* correl *_pr_* if year==2017 * 
* correl *_pr_* if year==2018 *
* correl *_pr_* if year==2019 *
* correl *_pr_* if year==2020 *


* ---------------------------------------------------------------* 
* Range of Prices in within exchange by year * 
* ---------------------------------------------------------------* 

sum kr_diff bs_diff bf_diff cb_diff if year==2017
sum kr_diff bs_diff bf_diff cb_diff if year==2018
sum kr_diff bs_diff bf_diff cb_diff if year==2019
sum kr_diff bs_diff bf_diff cb_diff if year==2020
sum kr_diff bs_diff bf_diff cb_diff if year==2021


* ---------------------------------------------------------------* 
* Differences in average prices between exchanges by year * 
* ---------------------------------------------------------------* 

sum bs_kr_diff kr_bs_diff bf_kr_diff kr_bf_diff bs_bf_diff bf_bs_diff bf_cb_diff cb_bf_diff bs_cb_diff cb_bs_diff kr_cb_diff cb_kr_diff if year==2017
sum bs_kr_diff kr_bs_diff bf_kr_diff kr_bf_diff bs_bf_diff bf_bs_diff bf_cb_diff cb_bf_diff bs_cb_diff cb_bs_diff kr_cb_diff cb_kr_diff if year==2018
sum bs_kr_diff kr_bs_diff bf_kr_diff kr_bf_diff bs_bf_diff bf_bs_diff bf_cb_diff cb_bf_diff bs_cb_diff cb_bs_diff kr_cb_diff cb_kr_diff if year==2019
sum bs_kr_diff kr_bs_diff bf_kr_diff kr_bf_diff bs_bf_diff bf_bs_diff bf_cb_diff cb_bf_diff bs_cb_diff cb_bs_diff kr_cb_diff cb_kr_diff if year==2020
sum bs_kr_diff kr_bs_diff bf_kr_diff kr_bf_diff bs_bf_diff bf_bs_diff bf_cb_diff cb_bf_diff bs_cb_diff cb_bs_diff kr_cb_diff cb_kr_diff if year==2021


* ---------------------------------------------------------------* 
* Range of Cross-Prices between exchanges max-min average * 
* ---------------------------------------------------------------* 

*drop if interval_id==0 | interval_id==143 

*bs bf
sum bs_max_bf_min bf_max_bs_min if year==2017 
sum bs_max_bf_min bf_max_bs_min if year==2018 
sum bs_max_bf_min bf_max_bs_min if year==2019 
sum bs_max_bf_min bf_max_bs_min if year==2020 
sum bs_max_bf_min bf_max_bs_min if year==2021

*bs kr
sum bs_max_bf_min bf_max_bs_min if year==2017 
sum bs_max_bf_min bf_max_bs_min if year==2018 
sum bs_max_bf_min bf_max_bs_min if year==2019 
sum bs_max_bf_min bf_max_bs_min if year==2020 
sum bs_max_bf_min bf_max_bs_min if year==2021

*bs cb
sum bs_max_bf_min bf_max_bs_min if year==2017 
sum bs_max_bf_min bf_max_bs_min if year==2018 
sum bs_max_bf_min bf_max_bs_min if year==2019 
sum bs_max_bf_min bf_max_bs_min if year==2020 
sum bs_max_bf_min bf_max_bs_min if year==2021

*bf kr
sum bs_max_bf_min bf_max_bs_min if year==2017 
sum bs_max_bf_min bf_max_bs_min if year==2018 
sum bs_max_bf_min bf_max_bs_min if year==2019 
sum bs_max_bf_min bf_max_bs_min if year==2020 
sum bs_max_bf_min bf_max_bs_min if year==2021

*bf cb
sum bs_max_bf_min bf_max_bs_min if year==2017 
sum bs_max_bf_min bf_max_bs_min if year==2018 
sum bs_max_bf_min bf_max_bs_min if year==2019 
sum bs_max_bf_min bf_max_bs_min if year==2020 
sum bs_max_bf_min bf_max_bs_min if year==2021

*kr cb
sum bs_max_bf_min bf_max_bs_min if year==2017 
sum bs_max_bf_min bf_max_bs_min if year==2018 
sum bs_max_bf_min bf_max_bs_min if year==2019 
sum bs_max_bf_min bf_max_bs_min if year==2020 
sum bs_max_bf_min bf_max_bs_min if year==2021
#delimit cr

