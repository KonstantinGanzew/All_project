a = int(input())
b = int(input())
c = int(input())
d = int(input())
cord1 = 0
cord2 = 0
if a >= 0:
    if b >= 0:
        cord1 = 1
    else:
        cord1 = 4
else:
    if b >= 0:
        cord1 = 2
    else:
        cord1 = 3
if c >= 0:
    if d >= 0:
        cord2 = 1
    else:
        cord2 = 4
else:
    if d >= 0:
        cord2 = 2
    else:
        cord2 = 3
if cord1 == cord2:
    print('YES')
else:
    print('NO')
