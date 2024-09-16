def solution(order):
    answer = 0
    three = str(order).count('3')
    six = str(order).count('6')
    nine = str(order).count('9')
    answer = three + six + nine
    return answer