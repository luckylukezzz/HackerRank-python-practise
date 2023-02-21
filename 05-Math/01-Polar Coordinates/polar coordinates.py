#https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

import cmath
x=complex(input())
print("{}\n{}".format(abs(x),cmath.phase(x)))