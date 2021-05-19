def solution(s, n):
    answer = ''
    for c in s:
        if c!=' ':
            counter = n
            now = ord(c)
        
            while counter>0 :
                now+=1
                counter-=1
                if now ==123:
                    now =97
                if now == 91:
                    now = 65
            
            c = chr(now)
        answer +=c
    return answer

solution("AB",1)
