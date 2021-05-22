def solution(citations):
    answer = 0
    clen = len(citations)
    c_min = 0
    c_max = clen
    citations.sort()
    while c_min<=c_max:
        h = (c_min+c_max)//2
        print(c_min,c_max)
        for i in range(clen):
            
            if citations[i]>=h :
                #print (citations[i] , h , clen-i)
                # ciation[i]>=h(h번 인용된 논문의 첫 인덱스 = i)
                # clen -i ==h : (h번 인용된 논문의 개수가 h이면)
                if clen-i >=h:
                    answer = h
                    c_min=h+1
                    break
                else:
                    c_max=h-1
                    break
        else:
            
            c_max=h-1
            

    return answer



print(solution([5,5,5,5,5]))