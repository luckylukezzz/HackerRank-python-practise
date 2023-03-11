#https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true

import numpy
n,m=map(int,input().split())
ar1=numpy.array([input().split() for i in range(n)],int)
ar2=numpy.array([input().split() for i in range(n)],int)
print(ar1+ar2)
print(ar1-ar2)
print(ar1*ar2)
print(ar1//ar2)
print(ar1%ar2)
print(ar1**ar2)
