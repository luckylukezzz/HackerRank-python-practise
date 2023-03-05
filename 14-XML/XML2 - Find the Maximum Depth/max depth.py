#https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem?isFullScreen=true



maxdepth = 0
def depth(elem, level):
    global maxdepth
    for i in elem:
        depth(i, level+1)
    if maxdepth<(level+1):
        maxdepth=level+1  
