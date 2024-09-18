import sys
from collections import defaultdict
sys.setrecursionlimit(1000001)

A = defaultdict(list)
vis = [False] * 1000001

def dfs(u):
    vis[u] = True
    if not A[u]:
        return 1, 0
    
    on, off = 1, 0
    for v in [v for v in A[u] if not vis[v]]:
        child_on, child_off = dfs(v)
        on +=  min(child_on, child_off)
        off += child_on
    return on, off

def solution(n, lighthouse):
    for u, v in lighthouse:
        A[u].append(v)
        A[v].append(u)
    
    on, off = dfs(1)
    return min(on, off)