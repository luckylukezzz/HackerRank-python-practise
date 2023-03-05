#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
import re

n=int(input())
for i in range(n):
    string=input()
    def fun1(x):
        return "or" if x.group()=="||" else "and"
            

    print(re.sub(r"(?<= )(&&|\|\|)(?= )",fun1,string))
