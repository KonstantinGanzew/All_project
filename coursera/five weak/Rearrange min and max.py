a = list(map(int, input().split()))
b = a.index(max(a))
c = a.index(min(a))
a[b], a[c] = a[c], a[b]
print(*a)
