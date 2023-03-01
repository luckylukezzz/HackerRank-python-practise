#https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true

n=(input())
noList=list(map(int,input().split()))
for i in noList:
    if i<=0:
        x=False
        break
else:
    x=True    

for i in noList:
    if not "".join(reversed(str(i)))!=str(i):
        y=(True)
        break
else:
    y=False
    
print(all([x,y]))
