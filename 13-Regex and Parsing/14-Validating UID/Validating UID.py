#https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true

import re
for _ in range(int(input())):
    x=input()
    if len(x)==10 and not re.search(r"[^a-zA-Z0-9]",x):
        if len(re.findall(r"\d",x))>=3 and len(re.findall(r"[A-Z]",x))>=2:
            if not re.search(r"(.)(?=.*\1)",x):
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
