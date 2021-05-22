def solution(cacheSize, cities):
    answer = 0
    cache={}
    for i, c in enumerate(cities):
        c=c.lower()
        if c not in cache:
            answer+=5
            cache[c]=i
            min=500000
            mink=0
            if len(cache)>cacheSize:
                for k in cache:
                    if cache[k]<=min:
                        min = cache[k]
                        mink =k
                cache.pop(mink)
        else:
            answer+=1
            cache[c]=i

        
        
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))