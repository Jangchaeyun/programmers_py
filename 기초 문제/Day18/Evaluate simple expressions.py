def solution(binomial):
    a = None
    b = None
    op = None
    new_bnl = binomial.split()

    for idx, char in enumerate(new_bnl):
        if idx == 0:
            a = ''.join(char)
        
        elif idx == 1:
            op = ''.join(char)

        elif idx == 2:
            b = ''.join(char)
    
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    else:
        return int(a) * int(b)