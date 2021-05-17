def solution(left, right):
    answer = 0
    squares = []
    for i in range(32):
        squares.append(i**2)

    for i in range(left,right+1):
        if i in squares:
            answer-=i
        else:
            answer+=i
    return answer