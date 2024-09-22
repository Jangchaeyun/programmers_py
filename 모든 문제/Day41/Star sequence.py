from collections import Counter

def solution(a):
    answer = -1

    els = Counter(a)

    for k in els.keys():
        if els[k] <= answer:
            continue
        cnt = 0
        idx = 0
        while idx < len(a) - 1:
            if (a[idx] != k and a[idx + 1] != k) or (a[idx] == a[idx + 1]):
                idx += 1
                continue

            cnt += 1
            idx += 2
        
        answer = max(cnt, answer)
    
    return -1 if answer == -1 else answer * 2