def solution(n, m):
    
    nmmax = uclid_max(n,m)
    answer = [nmmax,n*m/nmmax]
    return answer

def uclid_max(a,b):
    if b>a:
        temp = a
        a=b
        b=temp
    
    if a%b != 0:
        return uclid_max(b,a%b)
    else:
        return b