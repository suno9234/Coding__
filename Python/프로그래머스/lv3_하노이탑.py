def solution(n):
    answer = []
    hanoi(n,1,3,answer)
    return answer

def hanoi(n , now , next,answer):
    total = set([1,2,3])
    total =total - set([now,next])

    if n==1:
        answer.append([now,next])
        return

    hanoi(n-1, now ,list(total)[0],answer)
    answer.append([now,next])
    hanoi(n-1,list(total)[0],next,answer)

print(solution(2))