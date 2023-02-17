#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
   
    vowels = 'AEIOU'

    kev_score = 0
    stu_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kev_score += (len(string)-i)
        else:
            stu_score += (len(string)-i)

    if kev_score > stu_score:
        print ("Kevin", kev_score)
    elif kev_score < stu_score:
        print ("Stuart", stu_score)
    else:
        print ("Draw")

