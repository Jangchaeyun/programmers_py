def solution(s):
    s = list(s)
    s.sort()
    s.reverse()
    return "".join(s)