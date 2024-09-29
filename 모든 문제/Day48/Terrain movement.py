import heapq

def solution(land, height):
    N = len(land)

    visited = [[False for _ in range(N)] for _ in range(N)]
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = []

    visit_count = 0
    max_count = N * N
    value = 0

    queue.append((0, 0, 0))

    while visit_count < max_count:
        val, x, y = heapq.heappop(queue)
        if visited[x][y]:
            continue
        visited[x][y] = True

        visit_count += 1
        value += val

        curent_height = land[x][y]

        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            next_height = land[nx][ny]

            if abs(next_height - curent_height) > height:
                heapq.heappush(
                    queue, (abs(next_height - curent_height), nx, ny)
                )
            else:
                heapq.heappush(queue, (0, nx, ny))
    
    return value