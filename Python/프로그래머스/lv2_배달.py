from collections import deque 
def solution(N, road, K):
    answer = 0
    total_distance =[500000 for i in range(N+1)]
    total_distance[1]=0
    distance=[[] for i in range(N+1)]
    for r in road:
        distance[r[0]].append([r[1],r[2]])
        distance[r[1]].append([r[0],r[2]])
    
    
    q = deque()
    q.append(1)

    while q:
        now = q.popleft()

        for n in  distance[now]:
            # 1=>n이 1->now->n보다 크면 바꿔줌
            # disance [edge][destination, distance]
            # n = tuple [ dest , dis]
            if total_distance[n[0]] > total_distance[now]+n[1]:
                total_distance[n[0]]=total_distance[now]+n[1]
                q.append(n[0])
    for i in range(1,len(total_distance)):
        if total_distance[i]<=K:
            answer+=1
    return answer

solution(5,	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)