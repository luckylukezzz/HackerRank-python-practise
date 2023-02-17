#https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(num):
    l=len(bin(num))-2
    for n in range(1,num+1):
        
        x=str(hex(n)).replace("0x","")
        y1=x.rjust(l)
        
        z=str(bin(n)).replace("0b","")
        y2=z.rjust(l)
        
        m=str(oct(n)).replace("0o","")
        y3=m.rjust(l)
        
        y4=str(n).rjust(l)
        print  (y4,y3,y1.upper(),y2)