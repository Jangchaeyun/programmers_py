import heapq

INF = 10**8 + 10
d = [[INF] * 1024 for _ in range(1004)]
adj = [[] for _ in range(1004)]
adjrev = [[] for _ in range(1004)]
trapidx = [-1] * 1004

def bitmask(state, idx):
    return (1 << trapidx[idx]) & state

def solution(n, start, end, roads, traps):
    for u, v, val in roads:
        adj[u].append((v,val))
        adjrev[v].append((u,val))
    
    for i in range(len(traps)):
        trapidx[traps[i]] = i
    
    heap = []
    d[start][0] = 0
    heapq.heappush(heap, (d[start][0], start, 0))
    while heap:
        val, idx, state = heapq.heappop(heap)
        if idx == end: return val
        if d[idx][state] != val: continue
        for nxt, dist in adj[idx]:
            rev = 0
            if trapidx[idx] != -1 and bitmask(state, idx): rev ^= 1
            if trapidx[nxt] != -1 and bitmask(state, nxt): rev ^= 1
            if rev: continue 
            nxt_state = state
            if trapidx[nxt] != -1: nxt_state ^= (1 << trapidx[nxt])
            if d[nxt][nxt_state] > dist + val:
                d[nxt][nxt_state] = dist + val
                heapq.heappush(heap, (d[nxt][nxt_state], nxt, nxt_state))
        
        for nxt, dist in adjrev[idx]:
            rev = 0
            if trapidx[idx] != -1 and bitmask(state, idx): rev ^= 1 
            if trapidx[nxt] != -1 and bitmask(state, nxt): rev ^= 1
            if not rev: continue
            nxt_state = state
            if trapidx[nxt] != -1: nxt_state ^= (1 << trapidx[nxt])
            if d[nxt][nxt_state] > dist + val:
                d[nxt][nxt_state] = dist + val
                heapq.heappush(heap, (d[nxt][nxt_state], nxt, nxt_state))
    
    return -1