def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        for g in s:
            if g == '(' or g =='[' or g=='{':
                stack.append(g)
            elif g==')' :
                if len(stack)==0:
                    break
                elif stack[-1]=='(':
                    stack.pop()
                else :
                    break
            elif g==']':
                if len(stack)==0:
                    break
                elif stack[-1]=='[':
                    stack.pop()
                else:
                    break
            elif g=='}':
                if len(stack)==0:
                    break
                elif stack[-1]=="{":
                    stack.pop()
                else:
                    break
        else:
            if len(stack)==0:
                answer+=1
        s=rotate(s)
    return answer


def rotate(s):
    return s[1:]+s[0]

print(solution(""))