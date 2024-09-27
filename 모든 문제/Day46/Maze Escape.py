from collections import deque

def solution(maps):
    answer = 0
    
    graph = [list(m) for m in maps]

    def bfs(start, end):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        queue = deque()
        queue.append(start)
        
        while (queue):
            now = queue.popleft()
            for i in range(len(move)):
                nextRow = now[0] + move[i][0]
                nextCol = now[1] + move[i][1]
                if (0 <= nextRow < N) and (0 <= nextCol < M) and (not visited[nextRow][nextCol]) and (graph[nextRow][nextCol] != 'X'):
                    visited[nextRow][nextCol] = visited[now[0]][now[1]] + 1
                    queue.append([nextRow, nextCol])
    
        return visited[end[0]][end[1]]
    
    N = len(graph)
    M = len(graph[0])
    
    for row in range(len(graph)):
        if ('S' in graph[row]):
            start = [row, graph[row].index('S')]
        if ('L' in graph[row]):
            lever = [row, graph[row].index('L')]
        if ('E' in graph[row]):
            end = [row, graph[row].index('E')]
             
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    distance1 = bfs(start, lever)
    distance2 = bfs(lever, end)

    if (distance1 == 0) or (distance2 == 0):
        answer = -1
    else:
        answer = distance1 + distance2

    return answer