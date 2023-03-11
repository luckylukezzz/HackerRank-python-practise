#https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    x=''
    for i in range(n):
        x=x+str(i+1)
    print(x)
