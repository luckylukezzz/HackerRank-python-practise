#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
M=int(input())
a=set(map(int,input().split()))
N=int(input())
b=set(map(int,input().split()))
x=a.intersection(b)
for i in x:
    a.remove(i)
    b.remove(i)
y=sorted((a.union(b)))
for i in y:
    print(i)
