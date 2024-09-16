def solution(h):
    answer = ''
    
    for i in range(h):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    
    return answer