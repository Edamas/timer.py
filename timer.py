import datetime as dt

clocks = '🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛'

def timer(mins):
    '''
    PRECISION TIMER 
    
    Once the timer function is called, 
    
    1- finish time is calculated as follows: 
       
        now + minutes = finish time
    
    2- Each loop recalculates:
    
        (remaining time - now) / remaining loops
    
    3- The process finishes with a little deviation
    (less than using just 'time.sleep(minutes)' methods)
    '''
    
    t1       = dt.datetime.now() + dt.timedelta(minutes=mins)
    marks    = len(clocks)

    print(clocks[-1], end='')
    
    for n in range(marks):
        time.sleep((t1-dt.datetime.now()).total_seconds()/(marks-n))   # timer adjusted to remaining time
        print(clocks[n], end='')
    
    print()
    return 
    
    
>> timer(60)
🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛 # finishing after 60 minutes (1h)
