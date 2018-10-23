import math


def MinDivisor(n):
    c = 2
    l = int(math.sqrt(n))
    if n <= 2:
        return n
    else:
        while c <= l:
            if n % c == 0:
                return c
            c += 1
    return n
a = int(input())
print(MinDivisor(a))
