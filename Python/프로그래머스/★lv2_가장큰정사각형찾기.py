import pprint as pp

def solution(board):
    answer=0
    v=len(board)
    h=len(board[0])
    for i in range(2,v+1):
        for j in range(2,h+1):
            ## 0~v-1
            ## 0~h-1
            if board[v-i][h-j]!=0:
                board[v-i][h-j]=min(board[v-i+1][h-j+1],board[v-i+1][h-j],board[v-i][h-j+1])+1
    
    for i in range(v):
        for j in range(h):
            if answer<board[i][j]:
                answer=board[i][j]
    pp.pprint(board)
    return answer**2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
