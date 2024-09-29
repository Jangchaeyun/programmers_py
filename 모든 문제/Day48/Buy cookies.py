def solution(cookie):
    answer = 0

    for i in range(len(cookie) - 1):
        left, right = i, i + 1
        left_sum, right_sum = cookie[i], cookie[i + 1]

        while True:
            if left_sum == right_sum and left_sum > answer:
                answer = left_sum
            if left > 0 and left_sum <= right_sum:
                left -= 1
                left_sum += cookie[left]
            elif right < len(cookie) - 1 and left_sum >= right_sum:
                right += 1
                right_sum += cookie[right]
            else:
                break
    return answer