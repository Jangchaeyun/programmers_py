def solution(numbers, n):
    for i in range(len(numbers) + 1):
        if sum(numbers[:i]) > n:
            return sum(numbers[:i])