#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

x=set(input().split())
xd=0
lol=int(input())
for i in range(lol):
    ct=0
    y= set(input().split())
    if len(x)>len(y):
        for z in y:
            if z in x:
                ct+=1
        if ct==len(y):
            xd+=1
print("True" if xd==lol else "False")