from collections import defaultdict

def solution(n, path, order):
    adj = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for a, b in path:
        adj[a].append(b)
        adj[b].append(a)

    parent = defaultdict(int)
    child = defaultdict(int)

    for o in order:
        parent[o[1]] = o[0]
    if 0 in parent.keys():
        return False
    
    stk = [0]

    while stk:
        curr = stk.pop()

        if curr in parent.keys() and not visited[parent[curr]]:
            child[parent[curr]] = curr
            continue

        visited[curr] = True

        for nxt in adj[curr]:
            if not visited[nxt]:
                stk.append(nxt)
        
        if curr in child.keys():
            stk.append(child[curr])
        
    if False in visited:
        return False
    else: return True