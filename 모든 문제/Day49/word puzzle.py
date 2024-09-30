import math

def solution(strs, t):
    INF = math.inf
    dp = [INF for _ in range(len(t)+1)]
    dp[0] = 0
    for i in range(1,len(t)+1):
        j = 0 if i < 5 else i - 5
        while j < i:
            if dp[j] + 1 < dp[i] and t[j:i] in strs:
                dp[i] = dp[j]+1
            j +=1
    return dp[len(t)] if dp[len(t)] != INF else -1