#https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    count=0
    for j in range(len(string)-len(sub_string)+1):
        l=[]
        for i in range(len(sub_string)):
            if (j+i)>(len(string)):
                break
            l.append(string[j+i])
        l=(''.join(l))
        if l==sub_string:
            count+=1
    return count        


