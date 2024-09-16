import math
box = []

def solution(n):
    for i in range(1, 11):
        answer = math.factorial(i)
        box.append(answer)

        if box[i - 2] < n < box[i - 1]:
            return i - 1
        elif box[i - 2] <= n <= box[i - 1]:
            return i