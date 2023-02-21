#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

for i in range(int(input())):
    a=input()
    aa=set(input().split())
    b=input()
    bb=set(input().split())
    ct=0
    for i in aa:
        if i in bb:
            ct+=1
    print("True" if ct==len(aa) else "False")
        