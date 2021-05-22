def solution(land):
    answer = 0
    if len(land)==1:
        return max(land[0])
    else:
        last = 0
        for l in range(len(land)-1):
            mylist=[]
            for i in range(4):
                temp = land[l+1][i]
                for j in range(4):
                    if i!=j:
                        if temp< land[l+1][i]+land[l][j]:
                            temp =land[l+1][i]+land[l][j]
                land[l+1][i]=temp
            
            
    answer = max(land[len(land)-1])
    return answer
    

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))