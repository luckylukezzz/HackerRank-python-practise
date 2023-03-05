#https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true



def person_lister(f):
    def inner(people):
        newlist=[]
        x=sorted(list(set([int(i[2]) for i in people])))
        for i in x:
            for _ in people:
                if int(_[2])==i:
                    newlist.append(_)
        return (f(i) for i in newlist )    
    return inner

