def solution(n, words):
    answer = []
    worddic ={}
    round = 1
    counter =1
    last =words[0][0]
    for w in words:
        
        if w[0] != last[-1]:
            return  [counter,round]
            
        if worddic.get(w) is None:
            worddic[w]=1
        else:
            return [counter,round]
        counter+=1
        if counter==n+1:
            counter-=n
            round+=1
        last = w
    else:
        return [0,0]


print(solution(3,	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))