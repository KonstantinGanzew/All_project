a = float(input())
n = int(input())


def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(a, n / 2)**2
    return a * power(a, n - 1)

print(power(a, n))
