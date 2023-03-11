#https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
import numpy
n=int(input())
x=numpy.array([input().split() for i in range(n)],float)
print(round(numpy.linalg.det(x),2))

