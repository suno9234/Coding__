def solution(arr):
    arr_min = min(arr)
    arr.remove(arr_min)
    if len(arr)==0:
        arr.append(-1)
    return arr

print(solution([4,3,2,1]))