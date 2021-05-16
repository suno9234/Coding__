def solution(N, stages):
    
    failed = {}
    for i in range(0,N+2):
        failed[i]=0
    failed.pop(0)
    
    for i in stages:
        failed[i]=failed[i]+1

    divider=0
    end = N+1

    while divider==0:
        divider = failed[end]
        end-=1

    for i in range(end,0,-1) :
        temp  = failed[i]
        divider += temp
        failed[i] = failed[i]/divider
        
    failed.pop(N+1)
    failed_item =failed.items()
    sorted_failed_item = sorted(failed_item,key=lambda x:x[1],reverse = True)
    
    answer =[]
    for item in sorted_failed_item:
        answer.append(item[0])

    return answer

stages=[2, 1, 2, 6, 2, 4, 3, 3]

print(solution(5,stages))