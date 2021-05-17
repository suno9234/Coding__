def solution(d, budget):
    answer = 0
    d.sort(reverse = True)
    while budget>0 and d:
        price = d.pop()
        if budget>= price:
            budget-= price
            answer+=1
    return answer

print(solution([1,3,2,5,4],9))