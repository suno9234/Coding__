def solution(arr):
    answer = []
    last = -1
    for i in range(len(arr)):
        if arr[i]!=last:
            answer.append(arr[i])
            last = arr[i]
    
    return answer

print(solution([1,1,3,3,0,1,1]))
