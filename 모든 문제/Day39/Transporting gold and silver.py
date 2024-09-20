def solution(a, b, g, s, w, t):
    answer = (10**9) * (10**5) * 4
    
    start = 0
    end = (10**9) * (10**5) * 4
    
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0 
        total = 0
        
        for i in range(len(g)):
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]
            
            move_cnt = mid // (now_time * 2)
            
            if mid % (now_time * 2) >= now_time:
                move_cnt += 1
                
            gold += now_gold if (now_gold < move_cnt * now_weight) else move_cnt * now_weight 
            silver += now_silver if (now_silver < move_cnt * now_weight) else move_cnt * now_weight
            total += now_gold + now_silver if (now_gold + now_silver < move_cnt * now_weight) else move_cnt * now_weight 
        
        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
        
    return answer