import math

def solution(n, k):
    answer = []
    number = [i for i in range(1, n + 1)]

    while number:
        perm = math.factorial(n - 1)
        idx = (k - 1) // perm
        answer.append(number.pop(idx))
        k = k % perm
        n -= 1
    
    return answer