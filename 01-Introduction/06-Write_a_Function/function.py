#https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true


            #1 st method
def is_leap(year):
    leap = False
    if year%4==0:
        if year%100==0:
            if year%400==0: 
                leap=True
        else:
            leap=True
    return leap

    
        #2nd method
def is_leap(year):
    import calendar
    
    x=(calendar.isleap(year))
    return x