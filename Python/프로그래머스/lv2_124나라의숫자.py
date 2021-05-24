def solution(n):
    origin =n
    answer=""
    while n>0:
        temp =(n-1)%3
        if temp==0:
            temp=1
        elif temp==1:
            temp=2
        elif temp ==2:
            temp=4
        answer+=str(temp)
        n=(n-1)//3
    print(origin, answer[::-1])

for i in range(1,20):
    solution(i)