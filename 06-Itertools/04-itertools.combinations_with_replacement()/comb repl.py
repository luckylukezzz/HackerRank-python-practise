#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true



from itertools import combinations_with_replacement
x=input()
y=[]
li=[]
for i in x:
    if i.isalpha():
        y.append(i)
    elif i.isdigit():
      z=int(i)

li=sorted(list(map(sorted,combinations_with_replacement(y,z))))

for i in li:
    print("".join(i))