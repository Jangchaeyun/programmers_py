def solution(my_string):
    dic = {}
    for i in my_string:
        dic[i] = 1
    return ''.join(dic.keys())