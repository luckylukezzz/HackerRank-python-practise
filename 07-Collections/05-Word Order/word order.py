#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

from collections import OrderedDict
dct = OrderedDict()
n=int(input())
for i in range(n):
  x=input()
  dct[x]=(dct[x]+1 if x in dct else 1 )
print(len(dct.keys()))
print(*dct.values())