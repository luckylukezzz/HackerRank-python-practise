#https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
import re
n=int(input())
for i in range(n):
    x=input()
    y=re.search(r"^[\+\-]?\d*\.\d+$",x)
    print(True if y else False)
        