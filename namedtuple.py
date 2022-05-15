num= int(input())

from collections import namedtuple

std=namedtuple("std",input())
p=[]
count=0
for i in range(num):
  p.append(std(*(input().split())))
  count+=int(p[i].MARKS)
print("%.2f"%(count/num))

