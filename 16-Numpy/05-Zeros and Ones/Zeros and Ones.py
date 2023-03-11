#https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
import numpy
n=list(map(int,input().split()))
print(numpy.zeros(n,dtype=int))
print(numpy.ones(n,dtype=int))

