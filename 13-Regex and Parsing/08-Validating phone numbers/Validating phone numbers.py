#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true

import re

for _ in range(int(input())):
    
    m = re.search(r'^[789]\d{9}$', input().strip())
    print("YES" if m else "NO")
