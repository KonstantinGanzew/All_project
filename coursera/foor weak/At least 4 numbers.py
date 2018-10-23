def min4(a, b, c, d):
    aa = min(a, b)
    bb = min(c, d)
    cc = min(aa, bb)
    return cc
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
