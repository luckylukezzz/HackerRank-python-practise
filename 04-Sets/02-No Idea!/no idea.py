
n=(input().split())
arr=input().split()
a=set(input().split())
b=set(input().split())
count=0
for i in arr:
    if i in a:
        count+=1
    if i in b:
        count-=1
print(count)
