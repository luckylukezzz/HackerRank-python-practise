#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

for i in range(int(input())):
    a=input()
    Set_A=set(input().split())
    b=input()
    Set_B=set(input().split())
    count=0
    for i in Set_A:
        if i in Set_B:
            count+=1
    print("True" if count==len(Set_A) else "False")
        