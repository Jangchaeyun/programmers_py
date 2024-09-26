from collections import defaultdict

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
MOD = 1000000007

def matmul(mat1, mat2) :
    result = [[0]*L for _ in range(L)]
    for i in range(L) :
        for j in range(L) :
            for k in range(L) :
                result[i][j] = (result[i][j] + mat1[i][k] * mat2[k][j] ) % MOD
    return result

def matpow(mat, k) :
    if k == 1 :
        return mat
    p = matpow(mat, k // 2)
    p = matmul(p, p)
    if k % 2 :
        return matmul(p, mat)
    else :
        return p

def dfs(grid, d, r, c, idx, dp) :
    global R, C
    coord = r*C + c
    if idx == len(d) :
        return { coord : 1 }
    
    if dp[idx][coord] :
        return dp[idx][coord]
    
    for k in range(4) :
        ar, ac = r + dr[k], c + dc[k]
        if -1 < ar < R and -1 < ac < C and grid[ar][ac] - grid[r][c] == d[idx] :
            result = dfs(grid, d, ar, ac, idx+1, dp)
            for key, val in result.items() :
                dp[idx][coord][key] = ( dp[idx][coord][key] + val ) % MOD
    return dp[idx][coord]
        
def find_pattern(grid, d, k) :
    dp = [[defaultdict(int) for _ in range(L)] for _ in range(len(d))]
    for r in range(R) :
        for c in range(C) :
            dfs(grid, d, r, c, 0, dp)
            
    mat = [[dp[0][i][j] % MOD for j in range(L)] for i in range(L)]
    mat = matpow(mat, k)
    answer = 0
    for i in range(L) :
        for j in range(L) :
            answer = (answer + mat[i][j]) % MOD

    return answer

def solution(grid, d, k):
    global R, C, L
    R, C = len(grid), len(grid[0])
    L = R * C
    answer = find_pattern(grid, d, k)
    return answer