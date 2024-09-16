def solution(num_list, n):
    answer = 0

    for i in num_list:
        if n == i:
            return 1
    return answer