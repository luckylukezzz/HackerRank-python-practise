#https://www.hackerrank.com/challenges/nested-list/problem



if __name__ == '__main__':
    name=[]
    score=[]
    for _ in range(int(input())):
        
        
        name.append(input())
        score.append(float(input()))
        
    li=[]    
    for i in range(len(name)):
        li.append([name[i],score[i]])
        
    sortscore=sorted(score)
    
    for i in sortscore:
        if i!=sortscore[0]:
            sec=i
            break   
    namesec=[]   
    for i in li:
        if sec in i:
            namesec.append(i[0])
    
    
    print('\n'.join(sorted(namesec)))