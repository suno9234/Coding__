def solution(n, lost, reserve):
    answer = 0
    total = list(range(1,n+1))
    for p in total:
        if p in lost and p in reserve:
            lost.remove(p)
            reserve.remove(p)
    for p in total:
        if p in lost:
            if p-1 in reserve:
                answer = answer+1
                reserve.remove(p-1)
            elif p+1 in reserve:
                answer = answer+1
                reserve.remove(p+1)
        else:
            answer=answer+1
            

    
    return answer
