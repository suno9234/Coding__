def solution(n):
    if n // (n**0.5) != (n**0.5):
        return -1
    else:
        return int((n**0.5+1)**2)
