def solution(s):
    answer = True
    stack =[]
    for c in s:
        
        if c=='(':
            stack.append(c)
        else:
            if stack:
                if stack.pop()==c:
                    return False
            else:
                return False
    if stack:
        return False
    return True

print(solution("(())()"))