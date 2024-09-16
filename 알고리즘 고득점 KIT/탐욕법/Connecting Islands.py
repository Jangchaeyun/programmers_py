import heapq

def solution(n, costs):
    graph = [[] for _ in range(n)]
    for cost in costs:
        graph[cost[0]].append((cost[1], cost[2]))
        graph[cost[1]].append((cost[0], cost[2]))
    
    start = 0
    visited = [False] * len(graph)
    visited[start] = True
    heap = []
    result = 0

    for node, weight in graph[start]:
        heapq.heappush(heap, (weight, start, node))

    while heap:
        weight, start, node = heapq.heappop(heap)
        if visited[node]:
            continue

        visited[node] = True
        result += weight

        for next_node, next_weight in graph[node]:
            heapq.heappush(heap, (next_weight, node, next_node))
    
    return result