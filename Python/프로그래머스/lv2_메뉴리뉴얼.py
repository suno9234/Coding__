from itertools import combinations
def solution(orders, course):
    
    def func(liststring):
        answer = ""
        
        for i in liststring:
            answer+=i
        answer= "".join(sorted(answer))
        return answer
    
    answer = []
    for c in course:
        _order =[]
        for order in orders:
            if len(order)>=c:
                _order.append(order)
        comb ={}
        
        for order in _order:
            comblist =list(map(func ,combinations(order,c)))
            for l in comblist:
                if comb.get(l) is None:
                    comb[l]=1
                else:
                    comb[l]=comb[l]+1
    
        max =0
        maxs=[]
        for com in comb:
            if comb[com]>max:
                max=comb[com]
                maxs=[]
                maxs.append(com)
            elif comb[com]==max:
                maxs.append(com)

        for i in maxs:
            if comb[i]>1:
                answer.append(i)
    answer=sorted(answer)
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))