#https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

n,x=map(int,input().split())
z=[]
for i in range(x):
    z.append(list(map(float,input().split())))
m=zip(*z)

for i in m:
    print("{:.1f}".format((sum(i)/x)))