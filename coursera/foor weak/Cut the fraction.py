import math


def ReduceFraction(n, m):
    k = math.gcd(n, m)
    return (n // k, m // k)

a = ReduceFraction(int(input()), int(input()))
print(a[0], a[1])
