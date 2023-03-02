#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true
import re
vow='aeiou'
con="qwrtypsdfghjklzxcvbnm"
x=re.findall(r"(?<=[{1}])[{0}][{0}]+(?=[{1}])".format(vow,con),input(),re.I)

if not x:
    print (-1)
else:
    for i in x:
        print(i)
