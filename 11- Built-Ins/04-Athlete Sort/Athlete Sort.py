#https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n,m = map(int,input().split())


    list1 = []

    for _ in range(n):
        list1.append(list(map(int, input().rstrip().split())))

    k = int(input())
    z=[]
    for i in list1:
        z.append(i[k])
    newList=[]
    for i in sorted(set(z)):
        for j in list1:
            if j[k]==i:
                newList.append(j)
    for i in newList :
        print(*i)
