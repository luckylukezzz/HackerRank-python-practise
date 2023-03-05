#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true
import re
def wrapper(f):
    def fun(l):
        z=[]
        for i in l:
            if len(i)>10:
                x=re.sub("^(0|91|\+91)(?=.{10})","+91",i)
            else:
                x="+91"+i
            z.append(x[0:3]+" "+x[3:8]+" "+x[8:])    
        return f(z)
    return fun

