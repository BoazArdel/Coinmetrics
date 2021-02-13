#delimit ; ;

set more off ;
set memory 600m  ;
capture log close ;

pwd ;


log using data_2020.log, replace ;

set matsize 150 ;


use Year_2020_correct_format.dta   ;


* ---------------------------------------------------------------* ;
* ---------------------------Notation ---------------------------* ;

* bs will be abbreviation of bitstamp * ;
* bf will be abbreviation of bitfinex * ;
* bs_kr = avg_pr_bs  - avg_pr_kr  * ;
* ----------------------------------------------------------------* ;

gen bs_kr_avg = avg_pr_bs  - avg_pr_kr ;


gen kr_diff = max_pr_kr - min_pr_kr ;
gen bs_diff = max_pr_bs - min_pr_bs ;

gen bs_max_kr_min =  max_pr_bs - min_pr_kr ;
gen kr_max_bs_min =  max_pr_kr - min_pr_bs ;




* ---------------------------------------------------------------* ;
* Beginning the Analysis - descriptive and correlations * ;
* ---------------------------------------------------------------* ;

* ---------------------------------------------------------------* ;
* Corelations in Prices * ;
* ---------------------------------------------------------------* ;


correl *_pr_*;


* ---------------------------------------------------------------* ;
* Range of Prices within exchange * ;
* ---------------------------------------------------------------* ;

sum kr_diff bs_diff ;

* ---------------------------------------------------------------* ;
* Range of Cross-Prices between exchanges max-min average * ;
* ---------------------------------------------------------------* ;


sum bs_max_kr_min kr_max_bs_min , detail ;

sum  bs_kr_avg , detail ;

#delimit cr

