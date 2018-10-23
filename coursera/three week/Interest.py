a = int(input())
b = int(input())
c = int(input())
d = b * 100 + c
e = int(d / 100 * a)
f = int((d + e) // 100)
ff = int((d + e) % 100)
print(f, ff)
