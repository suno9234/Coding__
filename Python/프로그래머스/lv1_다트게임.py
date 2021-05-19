def solution(dartResult):
    answer =0
    
    score=[]
    oper=[]
    temp =""
    for c in dartResult:
        
        
        if c == 'S':
            temp=int(temp)
            score.append(temp)
            oper.append(1)
            temp=""
        elif c=='D':
            temp = int(temp)
            temp =temp**2
            score.append(temp)
            oper.append(1)
            temp=""
        elif c=='T':
            temp = int (temp)
            temp = temp**3
            score.append(temp)
            oper.append(1)
            temp=""
        elif c=='*':
            oper[-1]*=2
            if len(oper)>1:
                oper[-2]*=2
        elif c=='#':
            oper[-1]*=-1
        else:
            temp+=c
        

    """
    S = ^1
    D = ^2
    T = ^3

    * = 해당 점수와 바로 전에 얻느 점수 두배
    # = 해당 점수 마이너스
    
    """

    for i in range(len(oper)):
        answer+=oper[i]*score[i]
    
    return answer

print(solution("1S2D*3T"))