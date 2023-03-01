#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x**3


def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b