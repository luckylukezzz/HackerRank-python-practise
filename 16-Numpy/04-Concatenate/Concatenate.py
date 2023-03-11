#https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true

import numpy
n,m,p=map(int,input().split())
print(numpy.array([input().split() for i in range(m+n)],int))


