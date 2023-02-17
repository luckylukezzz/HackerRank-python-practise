#https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def print_rangoli(n):
    
    l1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    l2=[]
    l3=[]
    for m in reversed(range(1,n)):
    
        for j in range(m,n):
            l2.extend(l1[j])
        for i in reversed(range(m+1,n)):
            l3.extend(l1[i])
        l4=("-".join(l3+l2)).center(((n+(n-1))-1)+n+(n-1),"-")
        
        print(l4)
        l2=[]
        l3=[]
        l4=""



    for i in range(n):
        l2.extend(l1[i])
    for i in reversed(range (n-1)):
        l3.extend(l1[i+1])
    
    l4=("-".join(l3+l2)).center(((n+(n-1))-1)+n+(n-1))
    print(l4)

    l2=[]
    l3=[]
    l4=""
    for m in (range(1,n)):
  
        for j in (range(m,n)):
            l2.extend(l1[j])
        for i in reversed((range(m+1,n))):
            l3.extend(l1[i])
        l4=("-".join(l3+l2)).center(((n+(n-1))-1)+n+(n-1),"-")
        print(l4)
        l2=[]
        l3=[]
        l4=""

