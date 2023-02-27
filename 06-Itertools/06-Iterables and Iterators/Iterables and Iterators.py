#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true



from itertools import combinations


list1=[]
for i in range(1,int(input())+1):
  list1.append(i)

x=input().split()

l=list(combinations(list1,int(input())))

li_a=[]
for i in range(len(x)):
  if x[i]=="a":
    li_a.append(i+1)

count=0
for i in l:
  for j in li_a:
    if j in i:
      count+=1
      break

print("%.3f"%(count/len(l)))
