from itertools import permutations

def solution(numbers):
    answer =0
    prime =[True for i in range(9999999)]
    for i in range(2,len(prime)):
        if prime[i]==True:
            for j in range(i*2,len(prime),i):
                prime[j]=False
    prime[1]=False
    prime[0]=False

    numbers=list(numbers)
    Perm =[]
    for i in range(1,len(numbers)+1):
        perm = list(permutations(numbers,i))
        perm = set(["".join(j) for j in perm if j[0]!='0'])
        Perm+=perm
        
    for n in Perm:
        if prime[int(n)]:
            answer+=1

    return answer



solution("17")