a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = 0
a2 = len(a)
b1 = 0
b2 = len(b)
c = []
c1 = a1 + b1
while a1 != a2 and b1 != b2:
    if a[a1] < b[b1]:
        c.append(a[a1])
        a1 += 1
    else:
        c.append(b[b1])
        b1 += 1
if a1 != a2:
    while a1 != a2:
        c.append(a[a1])
        a1 += 1
else:
    while b1 != b2:
        c.append(b[b1])
        b1 += 1
print(*c)
