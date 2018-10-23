a = int(input())
b = int(input())


def sum(a, b):
    if b == 0:
        return a
    else:
        a += 1
        return sum(a, b - 1)

print(sum(a, b))
