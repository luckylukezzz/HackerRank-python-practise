
#https://www.hackerrank.com/challenges/py-set-mutations/problem

n=input()
x=set(input().split())
for i in range(int(input())):
    a,b=input().split()
    eval("x.{}({})".format(a,set(input().split())))

print(sum(map(int,x)))
