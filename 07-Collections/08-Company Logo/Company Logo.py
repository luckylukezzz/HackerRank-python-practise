#https://www.hackerrank.com/challenges/most-commons/submissions/code/270234081


from collections import Counter,defaultdict
x=Counter(input())
y=defaultdict(list)
for a,b in x.items():
  y[b].append(a)
for i in y.keys():
  y[i]=sorted(y[i])
mark=list(reversed(sorted(y.keys())))

count=0
  
for i in mark:
  for j in (y[i]):
    if count<3:
      print(j,i)
      count+=1
    else:
      break