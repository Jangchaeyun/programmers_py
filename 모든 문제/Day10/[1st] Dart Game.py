def solution(dartResult):
    answer = 0
    
    score = list()
    num = ''
    for i in dartResult:
        if (i == 'S'):
            score.append(int(num) ** 1)
            num = ''
        elif (i == 'D'):
            score.append(int(num) ** 2)
            num = ''
        elif (i == 'T'):
            score.append(int(num) ** 3)
            num = ''
        elif (i == '*'):
            if (len(score) == 1):
                score[0] *= 2
            else:
                score[-1] *= 2
                score[-2] *= 2
        elif (i == '#'):
            score[-1] *= -1
        else:
            num += i
            
    answer = sum(score)
    return answer