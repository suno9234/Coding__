def solution(s):
    answer = ''
    alist = []
    temp =0
    porm=1
    for c in range(len(s)):
        if '0'<=s[c]<='9':
            temp = temp*10+int(s[c])
        elif s[c]=='-':
            porm=-1
        
        if s[c]==' ' or c ==len(s)-1:
            temp*=porm
            if not alist:
                alist=[temp,temp]
            else:
                if temp<alist[0]:
                    alist[0]=temp
                if temp>alist[1]:
                    alist[1]=temp
            temp=0
            porm=1
        
    answer+=str(alist[0])+" "+str(alist[1])
    return answer

solution("1 2 3 4")