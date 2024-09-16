import math

def solution(number1, denom1, number2, denom2):
    number = denom1 * number2 + denom2 * number1
    denom = denom1 * denom2
    gcd = math.gcd(denom, number)
    return [number // gcd, denom // gcd]