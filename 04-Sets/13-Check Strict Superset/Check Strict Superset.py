#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

set_x=set(input().split())
count=0
num=int(input())
for i in range(num):
    ct=0
    set_y= set(input().split())
    if len(set_x)>len(set_y):
        for z in set_y:
            if z in set_x:
                ct+=1
        if ct==len(set_y):
            count+=1
print("True" if count==num else "False")