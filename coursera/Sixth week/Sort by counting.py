def CountSort(A):
    b = [0] * 101
    for i in A:
        b[i] += 1
    aa = []
    for i in range(101):
        aa += [i] * b[i]
    return aa


a = list(map(int, input().split()))
a = CountSort(a)
print(*a)
