#https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
x=""    
for i in range(m):
    for _ in range(n):
        x+=matrix[_][i]
m=re.sub(r"(?<=[a-z0-9])[^a-z0-9]+(?=[a-z0-9])",r" ",x,flags=re.I)
print(m)
