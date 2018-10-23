a = int(input())
b = int(input())
if a > b:
    print('NO')
else:
    c = a - 1
    d = b - c
    e = c // d
    e += 1
    c = e * d
    if b == c:
        print('YES')
    else:
        print('NO')
