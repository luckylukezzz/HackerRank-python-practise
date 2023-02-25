#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations
x=input()
y=[]
for i in x:
    if i.isalpha():
        y.append(i)
    elif i.isdigit():
      z=int(i)

li=sorted(list(permutations(y,z)))
for i in li:
    print("".join(i))