def solution(my_string, is_prefix):
    answer = 0
    tmp = [my_string[:i] for i in range(0, len(my_string))]
    for i in tmp:
        if is_prefix == i:
            answer = 1
    
    return answer