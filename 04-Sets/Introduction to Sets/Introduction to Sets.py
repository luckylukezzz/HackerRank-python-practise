#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):
    return ("%.3f" %(sum(set(array))/len(set(array))))

