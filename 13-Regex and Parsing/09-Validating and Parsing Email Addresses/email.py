#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true

import re
for _ in range(int(input())):
    n,e=input().split()
    m = re.search(r'^\<[a-z][\w\-.]+@[a-z]+\.[a-z]{1,3}\>$',e,re.I)
    if m:
        print(n,m.group())
