#https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true




def wrap(string, max_width):
    count=0
    x=''
    l=[]
    for i in string:
        x=x+i
        count+=1
        if count==max_width:
            l.append(x)
            x=''
            count=0
    l.append(x)
        
        
        
        
    return "\n".join(l)


