a = list(map(int, input().split()))
b = len(a)
c = []
e = 1
n = 0
for i in range(b // 2):
    c.append(a[e])
    e += 2
    c.append(a[n])
    n += 2
if len(a) % 2 != 0:
    c.append(a[len(a) - 1])
print(*c)
