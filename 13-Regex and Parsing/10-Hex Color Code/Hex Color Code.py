#https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

import re
y=""
for _ in range(int(input())):
    y+=input()
new=re.findall("(?<=\{).*?(?=\})",y)   
x=re.finditer(r"#[0-9A-F]{3}([0-9A-F]{3})?","".join(new),re.I)
for _ in x:
    print(_.group())
