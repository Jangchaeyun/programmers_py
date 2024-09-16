a, b = map(int, input().strip().split(' '))

if a >= -100000 and b <= 100000:
    print("a =", a)
    print("b =", b)
else:
    print("다시 입력해주세요.")