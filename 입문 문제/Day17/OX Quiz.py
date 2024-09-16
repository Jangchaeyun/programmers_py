def solution(quiz):
    answer = []
    for q in quiz:
        left, right = q.split("=")
        left = left.split()
        print(left)
        if left[1] == '+':
            if int (left[0]) + int(left[2]) == int(right):
                answer.append('O')
            else:
                answer.append('X')
        elif left[1] == '-':
            if int(left[0]) - int(left[2]) == int(right):
                answer.append('O')
            else:
                answer.append('X')
    return answer