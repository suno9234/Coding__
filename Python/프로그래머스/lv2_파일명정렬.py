def solution(files):
    answer = []
    def func(tup):
        index = tup[0]
        string = tup[1]
        string =string.lower()
        head=""
        body=""
        flag =0
        for s in string:
            if not '0'<=s<='9':
                if flag ==2:
                    break
                head+=s
                flag =1
            else:
                #숫자
                body+=s
                flag =2
        
        return head,int(body),head+str(index)
    
    temp =list(enumerate(files))
    temp.sort(key=func)
    answer =[temp[i][1] for i in range(len(temp))]  

    return answer

solution(["a000120","a012","a0012","abc1","foo010bar020.zip"])



