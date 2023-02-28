
#https://www.hackerrank.com/challenges/exceptions/problem

for _ in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(int(a/b))
    except ZeroDivisionError as e:
        print ("Error Code: integer division or modulo by zero")
    except ValueError as y:
        print ("Error Code:",y)
