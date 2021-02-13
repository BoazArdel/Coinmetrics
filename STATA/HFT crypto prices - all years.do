use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta"

***************************************************************************************************************************************************************************************
************************************************************************ mean, min, max price - 10 minutes interval *******************************************************************************************
***************************************************************************************************************************************************************************************

*rename secondssincemidnight seconds_count 
** take into account years for intervals **
replace seconds_count = seconds_count + (year-2015)*600000

** 10 minute time intervals - 600 seconds **

*gen interval = floor(seconds_count/600)+1



save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", replace

** Average prices at bitfinex **

keep if bf==1

collapse (mean) bitfinex_price_mean = price (min) bitfinex_price_min = price (max) bitfinex_price_max=price (mean) year, by( interval )

save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\bitfinex_prices.dta", replace

** Average prices at kraken **

use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear

keep if kr==1

collapse (mean) kraken_price_mean = price (min) kraken_price_min = price (max) kraken_price_max=price year, by( interval )

save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\kraken_prices.dta", replace


** Average prices at bitstamp **

use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear

keep if bs==1

collapse (mean) bitstamp_price_mean = price (min) bitstamp_price_min = price (max) bitstamp_price_max=price (mean) year, by( interval )

save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\bitstamp_prices.dta", replace

** merge prices from all exchanges to original DB **

use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear

merge m:1 interval using "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\bitfinex_prices.dta"
sort seconds_count
drop _merge

merge m:1 interval using "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\kraken_prices.dta"
sort seconds_count
drop _merge

merge m:1 interval using "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\bitstamp_prices.dta"
sort seconds_count
drop _merge

save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", replace

** differences in mean prices between exchanges **

gen bitfinex_kraken = bitfinex_price_mean - kraken_price_mean
gen bitfinex_bitstamp = bitfinex_price_mean - bitstamp_price_mean
gen kraken_bitstamp = kraken_price_mean - bitstamp_price_mean


***************************************************************************************************************************************************************************************
************************************************************************ mean side by exchange - 10 minute interval *******************************************************************************************
***************************************************************************************************************************************************************************************

**** bitfinex ****

use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear
keep if bf==1
collapse (mean) bitfinex_side_mean = side, by( interval )
save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\bitfinex_side_mean.dta", replace

**** kraken ****

use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear
keep if kr==1
collapse (mean) kraken_side_mean = side, by( interval )
save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\kraken_side_mean.dta", replace

**** bitstamp ****

use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear
keep if bs==1
collapse (mean) bitstamp_side_mean = side, by( interval )
save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\kraken_side_mean.dta", replace

***************************************************************************************************************************************************************************************
************************************************************************ wgt mean side by exchange - 10 minute interval *******************************************************************************************
***************************************************************************************************************************************************************************************

**** bitfinex ****

use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear
keep if kr==1
collapse (mean) bitfinex_side_wgt_mean = side [aweight=amount], by( interval )
save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\bitfinex_side_wgt_mean.dta", replace

**** kraken ****

use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear
keep if kr==1
collapse (mean) kraken_side_wgt_mean = side [aweight=amount], by( interval )
save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\kraken_side_wgt_mean.dta", replace

**** bitstamp ****

use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear
keep if bs==1
collapse (mean) bitstamp_side_wgt_mean = side [aweight=amount], by( interval )
save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\bitfinex_side_wgt_mean.dta", replace
***************************************************************************************************************************************************************************************
****************************************************************************** MERGE ALL MEAN SIDE *******************************************************************************************
***************************************************************************************************************************************************************************************


use "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", clear


merge m:1 interval using "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\bitfinex_side_mean.dta"
sort seconds_count
drop _merge

merge m:1 interval using "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\kraken_side_mean.dta"
sort seconds_count
drop _merge

merge m:1 interval using "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\bitfinex_side_wgt_mean.dta"
sort seconds_count
drop _merge

merge m:1 interval using "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\Exchanges_prices\kraken_side_wgt_mean.dta"
sort seconds_count
drop _merge

save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", replace

*rename bitfinex_price_mean bf_price_mean
*rename bitfinex_price_min bf_price_min
*rename bitfinex_price_max bf_price_max
*rename kraken_price_mean kr_price_mean
*rename kraken_price_min kr_price_min
*rename kraken_price_max kr_price_max
*rename bitfinex_kraken bf_kr
*rename bitfinex_side_mean bf_sell_mean
*rename kraken_side_mean kr_sell_mean
*rename bitfinex_side_wgt_mean bf_sell_wmean
*rename kraken_side_wgt_mean kr_sell_wmean

save "D:\Files\Google Drive (gabryu@gmail.com)\Projects\PycharmProjects\coinmetrics\15to20 bf bs kr stata data\All_data.dta", replace




