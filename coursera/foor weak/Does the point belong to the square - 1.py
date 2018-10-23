def IsPointInSquare(x, y):
    a = x <= 1.0 and x >= -1.0
    b = y <= 1.0 and y >= -1.0
    return a and b

a = float(input())
b = float(input())
if IsPointInSquare(a, b):
    print('YES')
else:
    print('NO')
