#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import defaultdict
od = defaultdict(list)
n=int(input())
for i in range(n):
  x=input().split()
  l1=[]
  for j in x:
    if j.isalpha():
      l1.append(j)
    else:
      price=int(j)  
  name=" ".join(l1)
  od[name].append(price)
for a,b in od.items():
  print(a, sum(b))
  
  
  
 # solution 2
  
from collections import OrderedDict
dct = OrderedDict()
for _ in range(int(input())):
    i = input().rpartition(" ")
    dct[i[0]] = int(i[-1]) + dct[i[0]] if i[0] in dct else int(i[-1])
for l in dct:
    print(l, dct[l])