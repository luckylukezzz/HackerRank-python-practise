#https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true

import numpy
numpy.set_printoptions(legacy="1.13")
r,c=map(int,input().split())
print (numpy.eye(r,c))
