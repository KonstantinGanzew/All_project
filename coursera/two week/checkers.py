x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
a = x1 - x
a1 = y1 - y
if a1 < 0:
    print('NO')
else:
    if a < 0:
        a = a * -1
    if a == 1 and a1 == 1:
        print('YES')
    else:
        print('NO')
