#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

from itertools import combinations
x=input()
y=[]
li=[]
for i in x:
    if i.isalpha():
        y.append(i)
    elif i.isdigit():
      no=int(i)
for _ in range(1,no+1):
  li += sorted( list( map( sorted,combinations(y,_))))

for i in li:
    print("".join(i))
