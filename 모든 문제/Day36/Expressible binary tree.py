def dfs(b, i, depth):
    if depth == 0:
        return True
    
    elif b[i] == '0':
        if b[i - depth] == '1' or b[i + depth] == '1': return False

    left = dfs(b, i - depth, depth // 2)
    rigjht = dfs(b, i + depth, depth // 2)
    return left and rigjht

def solution(numbers):
    answer = []
    for num in numbers:
        b = bin(num)[2:]
        nodes = bin(len(b) * 1)[2:]

        if '1' in nodes[1:]:
            dummies = (1 << len(nodes)) - int(nodes, 2)
            b = '0' * dummies + b
        
        result = dfs(b, len(b) // 2, (len(b) + 1) // 4)
        answer.append(1 if result else 0)
    
    return answer