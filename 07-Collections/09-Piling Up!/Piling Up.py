
#https://www.hackerrank.com/challenges/piling-up/submissions/code/270203482

from collections import deque
block=[]
d=deque()
for _ in range(int(input())):
  size=int(input())
  d.clear()
  d.extend(list(map(int,input().split())))
  block.clear()
  

  if d[0]>=d[-1]:
    block.append(d[0])
    d.popleft()
  

  else:
    block.append(d[-1])
    d.pop()
  for i in range(size-1):
    if (d[0]<=block[-1]) and (d[-1]<=block[-1]):
      if d[0]>=d[-1]:
        block.append(d[0])
        d.popleft()
      else:
        block.append(d[-1])
        d.pop()
        

    else:
      print("No")
      break
  if size==len(block):
    print("Yes")