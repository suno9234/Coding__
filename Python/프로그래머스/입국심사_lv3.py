def solution(n, times):
    answer = 0
    start = 0
    end = 1000000000000000000

    while start<=end :
        mid = (start+end)//2
        if isPossible(mid,times,n):
            answer = mid
            end = mid-1
        else:
            start = mid+1

    return answer

def isPossible(time,times,n):
    totalnum =0
    for simsa in times:
        totalnum+= time//simsa
        if(totalnum>=n):
            return True
    
    return False


# time 을 주고 그 시간 안에 할수 있는지 