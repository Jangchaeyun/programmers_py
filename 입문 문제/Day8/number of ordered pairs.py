def solution(n):
    answer = 0
    for i in range(1, n + 1):
        j = n % i
        if j == 0:
            answer += 1
        else:
            continue
    return answer