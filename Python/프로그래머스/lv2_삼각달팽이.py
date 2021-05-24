def solution(n):
    answer=[]
    temp = [[0 for j in range(n)] for i in range(n)]
    ## 0 1 3 6 10 15
    # 1
    # 2 15
    # 3 16 14
    # 4 17 21 13
    # 5 18 19 20 12
    # 6 7  8  9  10 11 
    x = 0 
    y = 0
    counter = n*(n+1)//2
    direction={1:(1,0),0:(0,1),-1:(-1,-1)}
    k=1       #down    right     up   
    d=1
    while(counter>0):
        temp[x][y]=k
        x+=direction[d][0]
        y+=direction[d][1]
        if d ==1 and x>=n :
            x-=direction[d][0]
            y-=direction[d][1]
            d=0
            x+=direction[d][0]
            y+=direction[d][1]    
        elif d==1 and temp[x][y]!=0:
            x-=direction[d][0]
            y-=direction[d][1]
            d=0
            x+=direction[d][0]
            y+=direction[d][1] 
        elif d==0 and y>=n:
            x-=direction[d][0]
            y-=direction[d][1]
            d=-1
            x+=direction[d][0]
            y+=direction[d][1] 
        elif d==0 and temp[x][y]!=0:
            x-=direction[d][0]
            y-=direction[d][1]
            d=-1
            x+=direction[d][0]
            y+=direction[d][1] 
        elif d==-1 and temp[x][y]!=0:
            x-=direction[d][0]
            y-=direction[d][1]
            d=1
            x+=direction[d][0]
            y+=direction[d][1] 
        counter-=1
        k+=1

    for i in range(0,n):
        for j in range(0,i+1):
            answer.append(temp[i][j])
    return answer

print(solution(4))