set more off 

use "\\Mac\Google Drive\Projects\GitHub\Coinmetrics\Data\full_data_4.4.dta", clear

* includes jan 2017 to march 2021, 1 min interval, bs, bf, kr, cb exchanges, btc to usd markets. 

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

*****gen kr_diff = (max_pr_kr - min_pr_kr)/min_pr_kr*100*****


gen bs_diff = (max_pr_bs - min_pr_bs)/avg_pr_bs*100 
gen bf_diff = (max_pr_bf - min_pr_bf)/avg_pr_bf*100 
gen cb_diff = (max_pr_cb - min_pr_cb)/avg_pr_cb*100 


* ----------------------------------------------------------------* 
* generating % differences between exchanges  * 
* ----------------------------------------------------------------* 

*****gen *_diff = |(avg_pr_bs  - avg_pr_kr)|/(the smaller)*****

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

* generating month_id * 

gen id = month
replace id = id+12 if year ==2018
replace id = id
replace id = id+24 if year ==2019
replace id = id+36 if year ==2020
replace id = id+48 if year ==2021
rename id month_id

* dropping first and last 5 intervals for each day

drop if interval_id < 6
drop if interval_id > 1434

* summary statistics and correlation calculations * 

*forvalues year = 2017/2021 {
*    forvalues month= 1/12 {
*        display `year'
*        display `month'
        * Corelations in Prices * 
*        correl *_pr_* if year==`year' & month==`month'
        * Range of Prices in within exchange by year * 
*        sum kr_diff bs_diff bf_diff cb_diff if year==`year' & month==`month'
        * Differences in average prices between exchanges by year * 
*        sum bs_kr_diff kr_bs_diff bf_kr_diff kr_bf_diff bs_bf_diff bf_bs_diff bf_cb_diff cb_bf_diff bs_cb_diff cb_bs_diff kr_cb_diff cb_kr_diff if year==`year' & month==`month'
        * Range of Cross-Prices between exchanges max-min average * 
*        sum bs_max_bf_min bf_max_bs_min if year==`year' & month==`month'
*        sum bs_max_kr_min kr_max_bs_min if year==`year' & month==`month'
*        sum bs_max_cb_min cb_max_bs_min if year==`year' & month==`month'
*        sum bf_max_kr_min kr_max_bf_min if year==`year' & month==`month'
*        sum bf_max_cb_min cb_max_bf_min if year==`year' & month==`month'
*        sum kr_max_cb_min cb_max_kr_min if year==`year' & month==`month'
*    }
*}

* creating max, min, avg variables for each difference variable *

foreach var of varlist *_diff {
    sum `var' if year ==2017 & month == 1 & `var' !=.
    gen max_`var'=r(max) if year ==2017 & month == 1 & `var' !=.
    gen min_`var'=r(min) if year ==2017 & month == 1 & `var' !=.
    gen avg_`var'=r(mean) if year ==2017 & month == 1 & `var' !=.
    forvalues year = 2017/2021{
        forvalues month = 1/12 {
            sum `var' if year == `year' & month == `month' & `var' !=.
            replace max_`var'=r(max) if year ==`year' & month == `month' & `var' !=.
            replace min_`var'=r(min) if year ==`year' & month == `month' & `var' !=.
            replace avg_`var'=r(mean) if year ==`year' & month == `month' & `var' !=.
        }
    }
}

* same, for *_min variables *
foreach var of varlist *_min {
    sum `var' if year ==2017 & month == 1 & `var' !=.
    gen max_`var'=r(max) if year ==2017 & month == 1 & `var' !=.
    gen min_`var'=r(min) if year ==2017 & month == 1 & `var' !=.
    gen avg_`var'=r(mean) if year ==2017 & month == 1 & `var' !=.
    forvalues year = 2017/2021{
        forvalues month = 1/12 {
            sum `var' if year == `year' & month == `month' & `var' !=.
            replace max_`var'=r(max) if year ==`year' & month == `month' & `var' !=.
            replace min_`var'=r(min) if year ==`year' & month == `month' & `var' !=.
            replace avg_`var'=r(mean) if year ==`year' & month == `month' & `var' !=.
        }
    }
}

* generating the arbitrage index:

egen min_vwap=rowmin(VWAP_cb VWAP_kr VWAP_bs VWAP_bf)
egen max_vwap=rowmax(VWAP_cb VWAP_kr VWAP_bs VWAP_bf)
gen arbitrage_index=max_vwap/min_vwap

twoway (line arbitrage_index month_id)

*calculating maximum of arbitrage index: 

sum arbitrage_index if year ==2017 & month == 1 & arbitrage_index !=.
gen max_arbitrage_index=r(max) if year ==2017 & month == 1 & arbitrage_index !=.
forvalues year = 2017/2021{
        forvalues month = 1/12 {
            sum arbitrage_index if year == `year' & month == `month' & arbitrage_index !=.
            replace max_arbitrage_index=r(max) if year ==`year' & month == `month' & arbitrage_index !=.
        }
}

 twoway (line max_arbitrage_index month_id)

* dropping to 51 observations- one for each month
duplicates drop month_id, force

drop avg_sec_bs avg_am_bs avg_pr_bs min_pr_bs max_pr_bs val_bs avg_sec_kr avg_am_kr avg_pr_kr min_pr_kr max_pr_kr val_kr avg_sec_bf avg_am_bf min_pr_bf max_pr_bf val_bf avg_sec_cb avg_am_cb avg_pr_cb min_pr_cb max_pr_cb val_cb VWAP_bs VWAP_bf VWAP_cb VWAP_cb VWAP_kr amount_btc_bs amount_btc_bf amount_btc_cb amount_btc_kr kr_diff bs_diff bf_diff cb_diff bs_kr_diff kr_bs_diff bf_kr_diff kr_bf_diff bs_bf_diff bf_bs_diff bf_cb_diff cb_bf_diff cb_kr_diff kr_cb_diff cb_bs_diff bs_cb_diff bs_max_kr_min bf_max_kr_min bs_max_bf_min kr_max_bs_min kr_max_bf_min bf_max_bs_min bf_max_cb_min cb_max_bf_min bs_max_cb_min cb_max_bs_min kr_max_cb_min cb_max_kr_min drop avg_pr_bf


*****volatility index: for the whole day, for each exchange




sum max_pr_bs if year ==2017 & month == 1 & max_pr_bs !=.
gen day_max_pr_bs =r(max) if year ==2017 & month == 1 & max_pr_bs !=.
forvalues year = 2017/2021{
        forvalues month = 1/12 {
            sum max_pr_bs if year == `year' & month == `month' & max_pr_bs  !=.
            replace day_max_pr_bs =r(max) if year ==`year' & month == `month' & max_pr_bs  !=.
        }
}

sum min_pr_bs if year ==2017 & month == 1 & min_pr_bs !=.
gen day_min_pr_bs =r(max) if year ==2017 & month == 1 & min_pr_bs !=.
forvalues year = 2017/2021{
        forvalues month = 1/12 {
            sum min_pr_bs if year == `year' & month == `month' & min_pr_bs  !=.
            replace day_min_pr_bs =r(max) if year ==`year' & month == `month' & min_pr_bs  !=.
        }
}



gen day_bs_ volatility = (day_max_pr_bs - day_min_pr_bs) / day_min_pr_bs
