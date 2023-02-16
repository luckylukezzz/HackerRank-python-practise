#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    arr=[]
    for i in range(int(input())):
        x=input()
        y=x.split()
        if 'insert' in y:
            arr.insert(int(y[1]),int(y[2]))
        elif "print" in y:
            print(arr)
        elif "remove" in y:
            arr.remove(int(y[1]))
        elif "append" in y:
            arr.append(int(y[1]))
        elif "sort" in y:
            arr.sort()
        elif "pop" in y:
            arr.pop()
        elif "reverse" in y:
            arr.reverse()