#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx=max(arr)
    run=-100
    for i in range(n):
        if arr[i]<mx:
            if arr[i]>=run:
                run=arr[i]
            
    print(run)
