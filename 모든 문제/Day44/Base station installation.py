def solution(n, stations, w):
    answer = 0
    std = w * 2 + 1
    start = 1
    for s in stations:
        if s - w - start > 0:
            answer += (s - w - start) // std
            if (s - w - start) % std: answer += 1
        start = s + w + 1
    if n - start + 1 > 0:
        answer += (n - start + 1) // std
        if (n - start + 1) % std: answer += 1
    return answer