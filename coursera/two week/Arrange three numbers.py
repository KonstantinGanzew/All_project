a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    print(a, b, c)
elif a < c < b:
    print(a, c, b)
elif b < a < c:
    print(b, a, c)
elif b < c < a:
    print(b, c, a)
elif c < a < b:
    print(c, a, b)
elif c < b < a:
    print(c, b, a)
elif a < b == c:
    print(a, b, c)
elif b < a == c:
    print(b, a, c)
elif c < a == b:
    print(c, a, b)
elif a > b == c:
    print(b, c, a)
elif b > a == c:
    print(a, c, b)
elif c > a == b:
    print(a, b, c)
else:
    print(a, b, c)
