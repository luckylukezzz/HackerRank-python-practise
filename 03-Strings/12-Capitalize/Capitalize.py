#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

def solve(s):
    
    
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s