from collections import Counter

x=int(input())
y=Counter(map(int,input().split()))


income=0
for i in range(int(input())):
  size,price=map(int,input().split())
  if size in y.keys():
    if y[size]!=0:
      income+=price
      y[size]-=1
print(income)