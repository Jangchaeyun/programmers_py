def solution(temperature, t1, t2, a, b, onboard):
    k = 1000 * 100
    t1 += 10
    t2 += 10
    temperature += 10
 
    DP = [[k] * 51 for _ in range(len(onboard))]
    DP[0][temperature] = 0
    
    flag = 1
    if temperature > t2 :
        flag = -1
 
    for i in range(1, len(onboard)):
        for j in range(51):
            arr = [k]
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                if 0 <= j+flag <= 50 :
                    arr.append(DP[i-1][j+flag])
                if j == temperature:
                    arr.append(DP[i-1][j])
                if 0 <= j-flag <= 50:
                    arr.append(DP[i-1][j-flag] + a)
                if t1 <= j <= t2:
                    arr.append(DP[i-1][j] + b)

                DP[i][j] = min(arr)
            
    answer = min(DP[len(onboard)-1])
    return answer