def solution(m, n, _board):
    answer = 0
    # mxn board

    board =[[0 for i in range(n)]for j in range(m)]
    for i in range(m):
        for j in range(n):
            board[i][j]=_board[i][j]
            
    
    eraser =set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                now =board[i][j]
                if now != '9' and  now ==board[i][j+1] and now == board[i+1][j] and now ==board[i+1][j+1]:
                    eraser.add((i,j))
                    eraser.add((i+1,j+1))
                    eraser.add((i,j+1))
                    eraser.add((i+1,j))
        
        if len(eraser)==0:
            break
        for e in eraser:
            x,y=int(e[0]),int(e[1])
            board[x][y]='0'
        for j in range(n):
            temp =""
            for i in range(m) :
                if board[i][j]!='0':
                    temp+=board[i][j]
            for i in range(len(temp)):
                board[m-i-1][j]=temp[-i-1]
            for i in range(m-len(temp)):
                board[m-i-1-len(temp)][j]='9'
        
        answer+=len(eraser)
        eraser.clear()
            
            


    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))