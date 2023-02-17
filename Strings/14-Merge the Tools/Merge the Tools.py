#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true


def merge_the_tools(s, k):
    b=[]

    for i in range (0,len(s),k):
        a=[]
        for j in range(k):
            a.append(s[i+j])
        b.append("".join(a))
    for i in b:
        l=[]
        for j in range(k):
            if i[j] not in l:
                l.append(i[j])
        print("".join(l))
    

