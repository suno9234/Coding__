from collections import deque
def solution(people, limit):
    answer = 0

    _people=deque()
    people.sort()
    

    while limit- people[-1]<40:
        people.pop()
        answer+=1
        if len(people)==0:
            break

    _people+=people


    while _people:
        now_max = _people.pop()
        if len(_people)>0:
            if _people[0]+now_max <=limit:
                _people.popleft()
        answer+=1
    return answer

print(solution([70,50,80,50,],100))

