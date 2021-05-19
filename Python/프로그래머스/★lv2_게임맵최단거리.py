import pprint as pp
from collections import deque as dq

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    distance = [[10001 for i in range(m)]for j in range(n)]
    distance[0][0]=1
    xy = [(1,0),(-1,0),(0,1),(0,-1)]
    queue=dq([])
    queue.append([0,0])
   
    while queue :
        nowX,nowY= queue.popleft()  
        for x,y in xy:
            newX = nowX+x
            newY = nowY+y
            # xy=>newx newy 갈꺼임
            if n>newX>=0 and m>newY >=0 and maps[newX][newY]!=0:
                if distance[newX][newY] > distance[nowX][nowY]+1:
                    distance[newX][newY] = distance[nowX][nowY]+1
                    queue.append([newX,newY]) 
                    """
                    append를 거리가 작을 때만 해야 한다. (방문한지 체크 안함)
                    """
                    # append는 거리가 작을 때만 한다 
        #pp.pprint(distance)
    answer = distance[n-1][m-1]
    if answer==10001:
        answer =-1
    return answer
    
    
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])