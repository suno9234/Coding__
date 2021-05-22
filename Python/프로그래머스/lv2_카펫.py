def solution(brown, yellow):
    answer = []
    # brown = 가로+세로 x2 -4
    # yellow = 전체 - brown
    
    total = (brown+4)/2
    ver = 1
    hor = total - ver

    while ver<=hor:
        if yellow == ver*hor - brown:
            break
        else:
            ver+=1
            hor =int(total-ver)
    
    answer.append(hor)
    answer.append(ver)
    return answer

solution(10,2)