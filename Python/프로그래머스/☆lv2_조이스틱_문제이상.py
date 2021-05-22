def solution(name):
    alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    name = list(name)
    _name =['A' for i in range(len(name))]
    answer = 0
    counter =0
    for i in name:
        if i != 'A':
            counter+=1
    now =0
    while counter>0 :
        if _name==name:
            break
        if _name[now]!=name[now]:
            temp =0
            for j in range(len(alphabet)):
                if alphabet[j] != name[now]:
                    temp+=1
                else:
                    break
            if temp>26-temp:
                temp = 26-temp
            answer += temp
            counter-=1
            _name[now]=name[now]
        else:
            temp =0
            left = 0
            right =0
            for i in range(1,len(name)):
                if _name[(now +i)%len(name)]!=name[(now+i)%len(name)]:
                    right = i
                    break
            for i in range(1,len(name)):
                if _name[now-i]!=name[now-i]:
                    left =i
                    break
            if left<=right:
                temp+=left
                now = (now-left)%len(name) 
                print("l "+str(left))
            else:
                temp+=right
                now = (now+right)%len(name)
                print("r "+str(right))
            answer+=temp

    return answer
       

print(solution("ZZAAAZZ"))