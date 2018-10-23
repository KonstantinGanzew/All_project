a = int(input())
b = int(input())
c = int(input())
d = int(input())
r = a - c
r1 = b - d
if r < 0:
    r = r**2
if r1 < 0:
    r1 = r1**2
if r <= 1 and r1 <= 1:
    print('YES')
else:
    print('NO')
