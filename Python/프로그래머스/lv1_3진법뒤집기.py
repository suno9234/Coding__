def solution(n):
    answer = 0
    nToStr =""
    while n>0:
        nToStr+=str(n%3)
        n=n//3
    multi=1
    nToStr=nToStr[::-1]
    for i in nToStr :
        answer+= int(i)*multi
        multi*=3


    return answer

print(solution(45))

