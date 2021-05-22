def solution(s):
    answer = [0,0]
    
    while s!='1':
        orilen=len(s)
        slen=0
        for c in s:
            if c =='1':
                slen+=1
        s=format(slen,'b')
        answer[0]+=1
        answer[1]+=orilen-slen
    return answer

solution("0111010")