def solution(s):
    answer = True
    s=s.lower()
    print(s)
    p=0
    y=0
    for c in s:
        if c=='p':
            p+=1
        elif c=='y':
            y+=1
    
    if p==0 and y==0:
        return True
    
    if p!=y:
        return False

    return True

solution("pPoooyY")