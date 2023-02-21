#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

from collections import Counter
y=input()
x=Counter(input().split())

for i in x.keys():
     if x[i]==1:
         print(i)
    
