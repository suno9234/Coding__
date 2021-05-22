def solution(msg):
    answer = []
    dic = {}
    aord = ord('A')
    diccounter=27
    for i in range(1,27):
        dic[chr(aord)]=i
        aord+=1
    while msg:
        counter=0
        temp =msg[counter]
        while dic.get(temp) is not None:
            if counter+1<=len(msg)-1:
                temp+=msg[counter+1]
                counter+=1
            else:
                break
        if len(temp) == len(msg) and dic.get(temp) is not None:
            msg=""
        if dic.get(temp) is None:
            dic[temp]=diccounter
            diccounter+=1
        if len(temp)>1:
            if msg=="":
                answer.append(dic[temp])
            else:
                answer.append(dic[temp[:-1]])
            msg = msg[len(temp)-1: ]
        else:
            answer.append(dic[temp])
            msg = msg[len(temp): ]

        
    return answer

print(solution("TOBEORNOTTOBEORTOBEORNOT"))