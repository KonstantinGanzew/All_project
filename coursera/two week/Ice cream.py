a = int(input())
c = a - ((a // 5 - 1) * 5)
e = a - ((a // 5 - 2) * 5)
if a % 3 == 0 or a % 5 == 0 or a % 8 == 0:
    if a == 0 or a == 1 or a == 2:
        print('NO')
    else:
        print('YES')
else:
    if a > 9:
        if c % 3 == 0 or c % 8 == 0:
            print('YES')
        else:
            if e % 3 == 0 or e % 8 == 0:
                print('YES')
            else:
                print('NO')
    else:
        print('NO')
