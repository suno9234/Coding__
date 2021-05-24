def solution(s):
    
    stack=[]
    for i in s:
        if len(stack)>0:
            if stack[-1] ==i:
                stack.pop() 
            else:
                stack.append(i)
        else:
            stack.append(i)

    if len(stack)>0:
        return 0
    else:
        return 1

