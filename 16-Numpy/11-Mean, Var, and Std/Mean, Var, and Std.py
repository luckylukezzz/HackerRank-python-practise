#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
import numpy
n,m=map(int,input().split())
x=numpy.array([input().split() for i in range(n)],int)
print(x.mean(axis=1))
print(x.var(axis=0))
print(round(x.std(),11))
