import math
import bisect
MOD = int(1e9 + 7)

def binary_search(arr, x):
    idx = bisect.bisect_left(arr, x)

    if idx == 0 and arr[idx] != x:
        return -1
    elif idx == len(arr):
        return -1
    else:
        return idx

def solve(b):
    maxb, n = max(b), len(b)

    ps = [0, b[0]]
    for i in range(1, n):
        ps.append(ps[-1] + b[i])
    
    maze = math.ceil(math.log2(ps[-1]))

    dp = [[0] * (maze + 1) for _ in range(n)]
    dp[0][0] = 1

    for i in range(1, n):
        dp[i][0] = sum(dp[i - 1])

        for e in range(1, maze + 1):
            if dp[i][e - 1] == 0:
                continue
            
            target = ps[i + 1] - b[i] * 2 ** (e - 1)
            jhalf = binary_search(ps, target)
            if jhalf == -1:
                continue

            eprime = math.log2(b[i] / b[jhalf - 1]) + (e - 1)
            if not eprime.is_integer() or eprime < 0:
                continue

            if not dp[jhalf - 1][int(eprime)] > 0:
                continue

            target = ps[i + 1] - b[i] * 2 ** e

            jfull = binary_search(ps, target)
            if jfull == -1:
                continue
            
            if jfull == 0:
                dp[i][e] = 1
            else:
                dp[i][e] = sum(dp[jfull - 1]) % MOD
    return sum(dp[-1]) % MOD

def solution(a, s):
    answer = []
    
    start = 0
    for l in s:
        b = a[start : start + l]

        answer.append(solve(b))

        start += l
    
    return answer