def solution(n, t, m, p):
    answer = ''
    total_answer="0"
    number = 1
    while len(total_answer)<t*m:

        temp=""
        _number =number
        while _number>0:
            if _number%n>=10:
                if _number%n==10:
                    temp+='A'
                elif _number%n==11:
                    temp+='B'
                elif _number%n==12:
                    temp+='C'
                elif _number%n==13:
                    temp+='D'
                elif _number%n==14:
                    temp+='E'
                elif _number%n==15:
                    temp+='F'
            else:
                temp+=str(_number%n)
            _number=_number//n
        
        total_answer+=temp[::-1]
        number= number+1
    for i in range(p-1,len(total_answer),m):
        answer+=total_answer[i]
    answer=answer[:t]
    return answer

print(solution(2,4,2,1))