#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
import re
s=input().strip()
p=input().strip()
if p not in s:
    print((-1,-1))
else:
    count=0
    while True: 
        m=re.search(r"{}".format(p),s)
        if m:
            
            print((m.start()+count,m.end()+count-1))
            count+=m.start()+1
            s=s[m.start()+1:]
            
        else:
            break  
