#https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true


import re
for _ in range(int(input())):
    x=input()
    m1 = re.search(r"(\d)\1{3,}",x.replace("-",""))
    if m1:
        print("Invalid")
    else:
        m = re.search(r'^[456]\d{3}(\-?)\d{4}\1\d{4}\1\d{4}$',x)
        print("Valid" if m else "Invalid")
