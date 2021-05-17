def solution(nums):
    answer = 0
    plus = []
    prime=[]

    for i in range(2,3001):
        prime.append(i)
        for j in range(len(prime)-1):
            if i % prime[j] ==0:
                prime.pop()
                break

    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                plus.append(nums[i]+nums[j]+nums[k])

    
    for i in plus:
        if i in prime:
            answer+=1


    return answer

