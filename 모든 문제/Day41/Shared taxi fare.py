import sys, heapq

def solution(n, s, a, b, fares):
    INF = sys.maxsize

    maps = [[] for _ in range(n+1)]
    for v,u,c in fares:
        maps[v].append((u, c))
        maps[u].append((v, c))
    
    def dijkstra(start):
        distance = [INF] * (n+1)
        distance[start] = 0
        que = [(0, start)]
        
        while que:
            cur_dist, cur_node = heapq.heappop(que)
            
            if distance[cur_node] < cur_dist:
                continue
            
            for next_node, next_dist in maps[cur_node]:
                if distance[next_node] > cur_dist + next_dist:
                    distance[next_node] = cur_dist + next_dist
                    heapq.heappush(que, (cur_dist + next_dist, next_node))         
        return distance
    
    D = [0] + [dijkstra(i) for i in range(1, n+1)] 
    
    path = INF
    for i in range(1, n+1):
        path = min(path, D[s][i] + D[i][a] + D[i][b])
       
    return path
