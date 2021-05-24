def solution(n):
    visited =[[False for i in range(n)]for j in range(n)]
    answer=[0]
    def func(row,maximum,visited,answer):
        def isPossible(x,y,visited):
            ver = len(visited)
            for i in range(row):
                if visited[i][y] and i!=x:
                    return False
            i=0 
            while i<row+1:
                if (x-i>=0 and y-i>=0) :
                    if visited[x-i][y-i]:
                        return False
                if x-i>=0 and y+i<ver:
                    if visited[x-i][y+i]:
                        return False
                i+=1
            return True

        if row==maximum:
            answer[0]+=1
            return
        for i in range(maximum):
            if isPossible(row,i,visited):
                visited[row][i]=True
                func(row+1,maximum,visited,answer)
                visited[row][i]=False

        
    func(0,n,visited,answer)
    return answer[0]

print(solution(4))