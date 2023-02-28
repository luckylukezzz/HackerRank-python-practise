import re
for _ in range(int(input())):
    
    try:
        reg = re.compile(input())
        print(True)
    except re.error:
        print(False)