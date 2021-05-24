def solution(n,a,b):
    answer = 0

    while True:
        answer+=1
        if a<b and b==a+1 and a%2!=0:
            return answer
        elif b<a and a==b+1 and b%2!=0:
            return answer

        if a%2==1:
            a+=1
        if b%2==1:
            b+=1
        a=a//2
        b=b//2
"""
def solution2(n,a,b):
    answer = 0
    if b<a:
        a,b= b,a
    while True:
        answer+=1
        if b==a+1:
            if a%2 ==0:
                answer+=1
            return answer
            
        if a%2==1:
            a+=1
        if b%2==1:
            b+=1
        a=a//2
        b=b//2

왜 틀린지 모름
"""

print(solution(8,2,3))
print(solution(8,1,2))
