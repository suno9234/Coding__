def solution(arr1, arr2):
    answer = [[0 for j in range(len(arr2[0]))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j]+=arr1[i][k] * arr2[k][j]
    return answer


print(solution([[1, 4], [3, 2], [4, 1]],	[[3, 3], [3, 3]]))
# 14
# 32  x  33
# 41     33

# 3x2  x 2x2 = 3x2 