def solution(my_string, overwite_string, s):
    answer = my_string[:s] + overwite_string + my_string[s + len(overwite_string):]
    return answer