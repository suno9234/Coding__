import datetime

def solution(a, b):
    answer=""
    first = datetime.datetime(2016,1,1)
    now = datetime.datetime(2016,a,b)

    f_n_mod = now - first
    day = f_n_mod.days%7

    if day == 0 :
        answer = "FRI"
    elif day == 1:
        answer = "SAT"
    elif day == 2:
        answer = "SUN"
    elif day == 3:
        answer = "MON"
    elif day == 4:
        answer = "TUE"
    elif day == 5:
        answer = "WED"
    elif day == 6:
        answer = "TUE"
    

    return answer



print(solution(1,3))


## 2016년 1월 1일 = 금요일
## 2016년 a월 b일은 무슨 요일?