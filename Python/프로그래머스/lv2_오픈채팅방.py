def solution(record):
    answer = []
    uid_nickname = {}
    for s in record :
        temp = list(s.split())
        oper = temp[0]
        uid = temp[1]
        if oper == "Enter" or oper =="Change":
            nickname = temp[2]
            uid_nickname[uid] =nickname
    
    for s in record : 
        temp = list(s.split())
        oper = temp[0]
        uid = temp[1]

        
        if oper =="Enter":
            answer.append(str(uid_nickname.get(uid))+"님이 들어왔습니다.")
        elif oper =="Leave":
            answer.append(str(uid_nickname.get(uid))+"님이 나갔습니다.")
            


    return answer

## 유저는 들어올때 uid와 닉네임으로 들어옴
## uid에 닉네임 관리하면 됨


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))