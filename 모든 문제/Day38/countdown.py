def solution(target):
    P = {}
    for i in range(1, 21):
        P[2 * i] = 0
        P[3 * i] = 0
    
    for i in range(1, 21):
        P[i] = 1
    P[50] = 1

    min_darts = [100001] * 100001
    max_sbs = [0] * 100001

    for i, sb in P.items():
        min_darts[i] = 1
        max_sbs[i] = sb
    
    for t in range(1, target + 1):
        if min_darts[t] != 100001:
            continue

        mn, sb = 100001, 0
        for score, _sb in P.items():
            if t - score < 0:
                continue

            s = t - score
            if (min_darts[s] + 1 < mn) or (min_darts[s] + 1 == mn and max_sbs[s] + _sb > sb):
                mn = min_darts[s] + 1
                sb = max_sbs[s] + _sb
        
        min_darts[t] = mn
        max_sbs[t] = sb
    
    return [min_darts[target], max_sbs[target]]