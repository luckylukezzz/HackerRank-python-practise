from collections import deque
d=deque()
for i in range(int(input())):
  x=input().split()
  if x[0]=="append":
    d.append(x[1])
  elif x[0]=="appendleft":
    d.appendleft(x[1])
  elif x[0]=="pop":
    d.pop()
  elif x[0]=="popleft":
    d.popleft()
  print(*d)