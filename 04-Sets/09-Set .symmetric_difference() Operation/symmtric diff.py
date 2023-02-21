#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true

c=input()
s=set(input().split())
d=input()
x=set(input().split())
print(len(s^x))
