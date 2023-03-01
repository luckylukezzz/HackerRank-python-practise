#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

sim=[]
cap=[]
od=[]
ev=[]
for i in input():
    if i.isdigit()==True:
        if eval(i)%2==0:
            ev.append(i)
        else:
            od.append(i)
    elif i.isupper()==True:
        cap.append(i)
    else:
        sim.append(i)
sim=sorted(sim)
cap=sorted(cap)
od=sorted(od)
ev=sorted(ev)
x=sim+cap+od+ev
print("".join(x))
