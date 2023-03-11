#https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true

import numpy
n,m=map(int,input().split())
x=numpy.array([input().split() for i in range(n)],int)
print(numpy.prod(numpy.sum(x,axis=0)))

