
#https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    x=[]
    for i in s:
        if i.isalpha()==True:
            if i.isupper()==True:
                x.append(i.lower())
            else:
                x.append(i.upper())
        else:
            x.append(i)
    
    return ("".join(x)) 


