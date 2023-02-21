#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math
x=float(input())
y=float(input())
print('%d\u00B0' %( int ( round (  math.degrees (  math.atan2(x,y)  )  )  ) ) )