#https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

import numpy
x=list(map(int,input().split()))
print(numpy.reshape(numpy.array(x),(3,3)))


