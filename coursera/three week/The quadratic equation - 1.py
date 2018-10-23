import math
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    a = x1 - math.floor(x1)
    b = x2 - math.floor(x2)
    if a == 0 and b == 0:
        if x1 > x2:
            print(int(x2), int(x1))
        else:
            print(int(x1), int(x2))
    else:
        if x1 > x2:
            print('{0:.6F}'.format(x2), '{0:.6F}'.format(x1))
        else:
            print('{0:.6F}'.format(x1), '{0:.6F}'.format(x2))
elif D == 0:
    x = (-b - math.sqrt(D)) / (2 * a)
    a = x - int(x)
    if a == 0:
        print(int(x))
    else:
        print(x)
else:
    pass
