#https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true


c=0
def get_attr_number(n):
    global c
    c+=len(n.attrib)
        
    for i in n:
        get_attr_number(i)
    return c   
    
