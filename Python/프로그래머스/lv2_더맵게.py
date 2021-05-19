import heapq as h

def solution(scoville, K):
    answer = 0
    h.heapify(scoville)
    while len(scoville)>=2:
        #print(scoville)
        m = h.heappop(scoville)
        if m>=K:
            return answer
        else:
            n = h.heappop(scoville)
            h.heappush(scoville,m+n*2)
            answer+=1

    if len(scoville)==1 and scoville[0]>=K:
        return answer

    return -1

print(solution([0,1],1))