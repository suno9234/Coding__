from collections import deque

def solution(n, edge):
    answer = 0
    graph = {}
    for x,y in edge:
        if graph.get(x) is not None:
            graph[x].append(y)    
        else:
            graph[x]=[y]

        if graph.get(y) is not None:
            graph[y].append(x)
        else:
            graph[y]=[x]

    distance = bfs(graph)[1:]
    maxdis = max(distance)

    for i in distance:
        if i == maxdis:
            answer+=1


    return answer


def bfs(graph):
    distance = [50000 for i in range(len(graph)+1)]
    distance[1]=0
    q =deque([])
    q.append(1)
    
    while len(q)>0 :
        last = q.popleft()
        print(last)
        
        for node in graph[last]: ## graph의 last노드에 연결되어 있는 노드에 대해
                # 1->node보다 1->last->node가 짧으면
            if distance[node]>distance[last]+1:
                distance[node]=distance[last]+1
                q.append(node)
        
    
    return distance
            
        







edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

solution(6,edge)