def solution(s):
    answer=''
    flag=0
    for c in s:
        if c!=' ':
            if flag==0:
                answer+=c.upper()
                flag =1
            else:
                answer+=c.lower()
                flag =0
        else:
            answer+=c
            flag =0
    return answer

print(solution("try hello world"))