def solution(x, n):
    if x==0:
        return[0 for i in range(n)]
    return [i for i in range(x,x*(n+1),x)]