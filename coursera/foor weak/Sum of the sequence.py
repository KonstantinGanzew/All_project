def summ(a):
    if a != 0:
        return a + summ(int(input()))
    return 0

print(summ(int(input())))
