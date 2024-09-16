def f(n, k):
    if n == 1:
        return k if k <= 2 else k - 1
    
    div = 5 ** (n - 1)
    mul = 4 ** (n - 1)
    loc = k // div

    if k % div == 0:
        loc -= 1
    
    if loc < 2:
        return mul * loc + f(n - 1, k - loc * div)
    elif loc == 2:
        return mul * loc
    else:
        return mul * (loc - 1) + f(n - 1, k - loc * div)

def solution(n, l, r):
    return f(n, r) - f(n, l - 1)