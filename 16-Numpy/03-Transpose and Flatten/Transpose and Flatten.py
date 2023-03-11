#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true

import numpy
r,c=map(int,input().split())

arr=numpy.array([input().split() for i in range(r)],int)
print(arr.transpose())
print(arr.flatten())
