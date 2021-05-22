from math import gcd

def solution(arr):
    while True:
        a = arr.pop()
        b = arr.pop()
        if not arr :
            return a*b//gcd(a,b)
        arr.append(a*b//gcd(a,b))
