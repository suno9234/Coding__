def solution(strings, n):
    answer=sorted(strings,key=lambda x:(x[n],x[0:n]+x[n+1:]))
    return answer
