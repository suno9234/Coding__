def solution(arr):
    answer = []
    answer=quad(arr,0,0,len(arr))
    return answer

def quad(arr,x,y,n):
    answer=[0,0]
    start = arr[x][y]
    for i in range(x,x+n):
        flag =1
        for j in range(y,y+n):
            if start!=arr[i][j]:
                qx,qy=quad(arr,x,y,n//2)
                answer[0]+=qx
                answer[1]+=qy

                qx,qy=quad(arr,x+n//2,y ,n//2)
                answer[0]+=qx
                answer[1]+=qy

                qx,qy=quad(arr,x,y+n//2,n//2)
                answer[0]+=qx
                answer[1]+=qy

                qx,qy=quad(arr,x+n//2,y+n//2,n//2)
                answer[0]+=qx
                answer[1]+=qy
                
                flag =0
                break
        if flag ==0:
            break
    else:
        if start==1:
            answer[1]+=1
        else:
            answer[0]+=1

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))