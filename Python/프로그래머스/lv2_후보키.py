from itertools import combinations
def solution(relation):
    answer = 0
    comb = [i for i in range(len(relation[0]))]
    key =[]
    for i in range(1,len(relation[0])+1):
        comb = list(combinations([j for j in range(len(relation[0]))],i))
        for c in comb:
            re_comb=[]
            flag =0
            for k in key:
                if set(k).issubset(c):
                    flag=1
                    break
            if flag ==1:
                continue
            for k in range(len(relation)):
                temp =[]
                for n in c:
                    temp.append(relation[k][n])
                re_comb.append(tuple(temp))
            
            if len(re_comb) == len(list(set(re_comb))):
                key.append(c)
    answer = len(key)     
    return answer

print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]))