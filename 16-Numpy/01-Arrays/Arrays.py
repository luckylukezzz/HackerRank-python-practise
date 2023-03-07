#https://www.hackerrank.com/challenges/np-arrays/problem

import numpy


def arrays(arr):
    x=numpy.array(arr,float)
    return x[-1::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)