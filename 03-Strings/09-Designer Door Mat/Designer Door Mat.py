
#https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = map(int,input().split())
y=1
for i in range (1,int((n-1)/2)+1):
    print((".|."*y).center(m,"-"))
    y+=2
print("WELCOME".center(m,"-"))
for i in range (1,int((n-1)/2)+1):
    y-=2
    print((".|."*y).center(m,"-"))
    