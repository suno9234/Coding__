import heapq
def solution(info, query):
    answer = []
    info_copy={}
    for i in info:
        info_token=i.split()
        l = info_token[0]
        b=info_token[1]
        j=info_token[2]
        f=info_token[3]
        s=info_token[4]
        c =l+b+j+f
        if info_copy.get(c) is None:
            info_copy[c]=[int(s)]
        else:
            info_copy[c].append(int(s))
    for key in info_copy:
        info_copy[key].sort()

    for q in query:
        tokens = q.split()
        language=[tokens[0]]
        if tokens[0]=='-':
            language=["java","python","cpp"]
        forb = [tokens[2]]
        if tokens[2]=='-':
            forb = ["frontend","backend"]
        jors = [tokens[4]]
        if tokens[4]=='-':
            jors=["junior","senior"]
        food = [tokens[6]]
        if tokens[6]=='-':
            food =["pizza","chicken"]
        score = int(tokens[7])
        counter=0
        for i in range(len(language)):
            for j in range(len(forb)):
                for k in range(len(jors)):
                    for l in range(len(food)):
                        find = language[i]+forb[j]+jors[k]+food[l]
                        if info_copy.get(find) is not None:
                            flist = info_copy[find]
                            start = 0
                            end = len(flist)-1
                            while start<=end:
                                mid = (start+end)//2
                                # flist = 들어있는 점수 score 내가 원하는 점수
                                if flist[mid]< score:
                                    start=mid+1
                                elif flist[mid]> score:
                                    end=mid-1
                                else:
                                    
                                    end = mid-1
                           
                            counter+=len(flist)-end-1
                                        

        answer.append(counter)

    print(answer)
    return answer

solution( ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])