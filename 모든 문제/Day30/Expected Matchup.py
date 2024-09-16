def solution(n, a, b):
    max_round = 0
    while 2 ** max_round < n:
        max_round += 1
    
    a, b = min(a, b), max(a, b)
    mid = n // 2
    lower = 0
    upper = n

    while True:
        if a <= mid and b > mid:
            break
        elif a >= mid:
            lower = mid
            mid = (mid + upper) // 2
            max_round -= 1
        
        elif b <= mid:
            upper = mid
            mid = (mid + lower) // 2
            max_round -= 1
    
    return max_round