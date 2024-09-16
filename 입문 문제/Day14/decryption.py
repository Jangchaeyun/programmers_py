def solution(ciper, code):
    answer = ''
    for i in range(code, len(ciper) + 1):
        if i % code == 0:
            print(i)
            answer += ciper[i - 1]
    return answer