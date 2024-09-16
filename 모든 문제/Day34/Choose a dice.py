from itertools import combinations, product

def solution(dice):
    n = len(dice)
    A, result = [], []
    cases = list(combinations(range(n), n//2))
    
    for case in cases:
        dices = [dice[c] for c in case]
        nums = sorted([sum(i) for i in product(*dices)])
        A.append(nums)
        
    a, p = 0, len(A)
    for i in range(p):
        B = A[p-i-1] 

        temp = 0
        for t in A[i]:
            left, right = 0, len(B)-1
            while left <= right:
                mid = (left + right) // 2
                if B[mid] < t:
                    left = mid + 1
                else :
                    right = mid - 1
            temp += left
    
        if a < temp:
            a = temp
            result = [x + 1 for x in cases[i]]
    
    return result