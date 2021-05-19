import pprint as pp

def solution(rows, columns, queries):
    answer = []
    arr = [[1+j+i*columns for j in range(columns)]for i in range(rows)]

    for query in queries:
        start = query[0]-1 , query[1]-1
        end = query[2]-1, query[3]-1

        temp = arr[start[0]][start[1]]
        numbers=[]
        numbers.append(temp)
        
        for i in range(end[0]-start[0]):
            arr[start[0]+i][start[1]] = arr[start[0]+i+1][start[1]]
            numbers.append(arr[start[0]+i+1][start[1]])
        arr[end[0]][start[1]]=arr[end[0]] [start[1]+1]
        numbers.append(arr[end[0]] [start[1]+1])

        for i in range(end[1]-start[1]):
            arr[end[0]][start[1]+i]=arr[end[0]][start[1]+i+1]
            numbers.append(arr[end[0]][start[1]+i+1])
        arr[end[0]][end[1]]=arr[end[0]-1][end[1]]
        numbers.append(arr[end[0]-1][end[1]])

        for i in range(end[0]-start[0]):
            arr[end[0]-i][end[1]]=arr[end[0]-i-1][end[1]]
            numbers.append(arr[end[0]-i-1][end[1]])
        arr[start[0]][end[1]]=arr[start[0]][end[1]-1]
        numbers.append(arr[start[0]][end[1]-1])

        for i in range(end[1]-start[1]-1):
            arr[start[0]][end[1]-i]=arr[start[0]][end[1]-i-1]
            numbers.append(arr[start[0]][end[1]-i-1])
        arr[start[0]][start[1]+1]=temp

        answer.append(min(numbers))
           
    return answer


solution(6,6,[[2,2,5,4]])