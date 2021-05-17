def solution(lottos, win_nums):
    answer = []
    zeros=0
    sames=0
    for numbers in lottos:
        if numbers == 0:
            zeros+=1
        elif numbers in win_nums:
            sames+=1
    
    lotto_max = sames+zeros
    lotto_min = sames
    
    if lotto_max <=1:
        lotto_max =1

    answer.append((7-lotto_max))

    if lotto_min <=1:
        lotto_min = 1
    answer.append((7-lotto_min))
    

    return answer
    

print(solution([1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]))

