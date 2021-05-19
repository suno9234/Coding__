def solution(n):
    isPrime = [True for i in range(n+1)]
    for i in range(2,int(n**(1/2))+1):
        if isPrime[i]:
            for j in range(i*2,n+1,i):
                isPrime[j]=False
    answer =0
    for i in isPrime[2:]:
        if i:
            answer+=1
        
    
    return answer
