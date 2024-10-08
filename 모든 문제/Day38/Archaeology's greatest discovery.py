from itertools import product

def solution(clockHands):
    answer = 9876543210
    n = len(clockHands)

    dy = [-1, 1, 0, 0, 0]
    dx = [0, 0, -1, 1, 0]

    def rotate(a, b, t, arr):
        for k in range(5):
            y, x = a + dy[k], b + dx[k]
            if 0 <= y < n and 0 <= x < n:
                arr[y][x] = (arr[y][x] + t) % 4

    for case in product(range(4), repeat=n):
        arr = [i[:] for i in clockHands]

        for j in range(n):
            rotate(0, j, case[j], arr)

        result = sum(case)

        for i in range(1, n):
            for j in range(n):
                if arr[i-1][j]:
                    temp = 4 - arr[i-1][j]
                    rotate(i, j, temp, arr) 
                    result += temp

        if sum(arr[n-1]):
            continue

        answer = min(answer, result)

    return answer