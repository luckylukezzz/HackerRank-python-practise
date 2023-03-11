#https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true
import numpy as a
a.set_printoptions(legacy="1.13")
x=a.array(input().split(),float)
print(a.floor(x))
print(a.ceil(x))
print(a.rint(x))
