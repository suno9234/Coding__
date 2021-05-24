from collections import deque
import pprint as pp
def solution(board):

    queue = deque()
    x,y=0,0
    distance=[[2000000 for j in range(len(board))]for i in range(len(board))]
    directions=[[9 for j in range(len(board))]for i in range(len(board))]
    distance[0][0]=0
    queue.append([0,0,0])
    # x좌표 y좌표 방향( -1 수직 1 수평 )
    xy = [[1,0],[-1,0],[0,1],[0,-1]]
    while queue:
        now =queue.popleft()
        
        for i in range(4):
            newX = now[0]+xy[i][0]
            newY = now[1]+xy[i][1]
            if 0<=newX<len(board) and 0<=newY<len(board) and board[newX][newY]!=1:
                cost =100
                direction = 0
                if newX ==now[0] :
                    # 가로로 이동
                    direction = 1
                    if directions[now[0]][now[1]]==-1 :
                        cost+=500
                elif newY == now[1] :
                    #세로로 이동
                    direction=-1
                    if directions[now[0]][now[1]] == 1 :
                        cost+=500
                if distance[newX][newY] > distance[now[0]][now[1]]+cost:
                    distance[newX][newY] = distance[now[0]][now[1]]+cost
                    queue.append([newX,newY,direction])
                    directions[newX][newY]=direction
                elif distance[newX][newY] == distance[now[0]][now[1]]+cost and  directions[newX][newY]!=direction:
                    directions[newX][newY] =0
                    queue.append([newX,newY,direction])
    return distance[len(board)-1][len(board)-1]

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))