#date iterator
from dateutil import rrule
from datetime import datetime, timedelta

def date_func (start_date, total_end_date):
    start_time = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S.%f000Z') #pharsed start_date
    total_end_time = datetime.strptime(total_end_date, '%Y-%m-%dT%H:%M:%S.%f000Z') #pharsed end_date

    #list of first wednesday of each month from start to end dates. 
    d_start = []
    for arg in rrule.rrule(rrule.MONTHLY, dtstart=start_time, interval=1, wkst=rrule.WE, until=total_end_time, bysetpos = 1, byweekday=rrule.WE):
        d_start.append(arg)
    #print(d_start)
    #print("finished")

    d_finish= []
    for date in d_start:
        d_finish.append(date + timedelta(days=1))
    

    #print(d_finish)

    #return lists to format
    p_d_start =[]
    for date in d_start:
        p_d_start.append(date.strftime("%Y-%m-%dT%H:%M:%S.%f000Z"))
    #print("this is parsed start dates list")
    #print(p_d_start)

    p_d_finish =[]
    for dates in d_finish:
        p_d_finish.append(dates.strftime("%Y-%m-%dT%H:%M:%S.%f000Z"))
    #print("this is parsed finish dates list")
    #print(p_d_finish)

    return p_d_start, p_d_finish

'''
#date iterator: same date one year.
mydates = []

date_list = range(1,13)

for i in range (0,12):
    if i<9:
        mydates.append ("2017-0" + str(date_list[i]) + "-15T00:00:00.000000000Z")
    else:
        mydates.append ("2017-" + str(date_list[i]) + "-15T00:00:00.000000000Z")

print(mydates)
'''
'''
#date iterator: same date all years
from dateutil import rrule
from datetime import datetime, timedelta

start_date = "2017-01-15T00:00:00.000000000Z"
start_time = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S.%f000Z')
#end_date = "2017-01-16T00:00:00.000000000Z"
#total_end_date = "2021-01-15T00:00:00.000000000Z"

hundredDaysLater = start_time + timedelta(days=100)

for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_time, until=hundredDaysLater):
    print(dt)
'''
