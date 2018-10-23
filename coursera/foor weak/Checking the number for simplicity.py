import math


def IsPrime(n):
    c = 2
    l = int(math.sqrt(n))
    if n <= 2:
        return True
    else:
        while c <= l:
            if n % c == 0:
                return False
            c += 1
    return True
a = int(input())
if IsPrime(a):
    print('YES')
else:
    print('NO')
