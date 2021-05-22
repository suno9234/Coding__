def solution(n):
    answer = 0
    i=1
    while True:
        
        now = n//i
        if (now - (i+1)//2) <0 :
            break
        if i%2 ==0 :
            left=0
            right=0
            for j in range(i//2):
                left +=now-j
            for j in range(i//2):
                right+=now+j+1
            if left+right ==n :
                answer+=1
        else:
            left =0
            right=0
            for j in range(i//2):
                left+=now-j-1
            for j in range(i//2):
                right+=now+j+1
            if left+right+now ==n:
                answer+=1
        
        i+=1

    return answer

solution(15)
    ## 15 = 15 78 456  12345
    ## 16 = 88 
    # n개의 연속된 숫자 k의 합 =   kn
    # n = 가운데 숫자 
    # 짝수개 =  1 2 4 8 16
    #         16     
    #
    #  홀수개 = 15> 1   3      5        15
    #              15  456   12345      1
    #
    #
    #

