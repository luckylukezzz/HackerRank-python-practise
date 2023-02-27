#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from itertools import product

li=[]
nolist,M=map(int,input().split())
for i in range(nolist):
  li.append(list(map(int,input().split())))
  li[i]=li[i][1:]
  
rand=list(product(*li))


allac=[]
for i in rand:
  s=0
  for j in i:
    s+=j**2
  s=s%M
  allac.append(s)
print(max(allac))