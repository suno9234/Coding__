def solution(s):
    answer = ''
    tokens = s.split(" ")
    for token in tokens:
        if token.isalnum():
            token =token.lower()
            if token[0].isalpha():
                if len(token)>1:
                    token=token[0].upper()+token[1:]
                else:
                    token=token[0].upper()
        answer+=token+" "
    return answer[:-1]

print(solution("3  people a unfo  me"))