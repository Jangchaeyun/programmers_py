import re

def solution(my_string):
    num = re.findall(r'\d+', my_string)
    num = list(map(int, num))
    return sum(num)