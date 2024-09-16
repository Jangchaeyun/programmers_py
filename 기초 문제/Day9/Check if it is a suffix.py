def solution(my_string, is_suffix):
    my = []
    for i in range(len(my_string)):
        my.append(my_string[i:])
    return 1 if is_suffix in my else 0