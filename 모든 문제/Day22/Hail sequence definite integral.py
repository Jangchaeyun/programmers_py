def getUbak(k):
    result = []
    while k != 1:
        result.append(k)
        k = k / 2 if k % 2 == 0 else k * 3 + 1 
    result.append(k)
    return result
 
def solution(k, ranges):
    answer = []
    ubak = getUbak(k)
 
    for r in ranges:
        total = 0
        ubakRange = ubak[r[0] : len(ubak)+r[1]]

        if r[0] >= r[1] + len(ubak):
            answer.append(-1)
            continue
            
        for i in range(len(ubakRange) - 1):
            total += (((ubakRange[i] + ubakRange[i+1]) * 1) / 2)
        answer.append(total)
        
    return answer
