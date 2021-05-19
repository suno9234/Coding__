def solution(w,h):
    if(w==h):
        return w*h-w
    elif(w==1 or h==1):
        return 0
    answer = w*h
    answer-=minus(w,h)
    return answer

def minus(w,h):
    answer=0
    uclidmax = uclid_max(w,h)
    if uclidmax !=1:
        return int(uclidmax*minus(w//uclidmax,h//uclidmax))
    for i in range(1,w+1):
        start = (i-1)*h/w
        end = i*h/w
        if start %1 !=0:
            start = start //1
        if end%1 !=0:
            end = end//1+1
        answer+=end-start
    return answer

def uclid_max (w,h):
    if h>w:
        temp = w
        w=h
        h=temp
    if w%h ==0:
        return h
    else:
        return uclid_max(h,w%h)

print(solution(8,12))
    
# y = h/w x
# (1, 1.5) 
# minus(w,h)=
# w는 짝수고 h는 홀수일경우
# minus(w,h)= minus(w/2+h//2)*2+
