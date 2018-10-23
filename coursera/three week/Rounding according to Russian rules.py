import math
a = float(input())
b = a % math.floor(a)
if b >= 0.5:
    print(math.ceil(a))
else:
    print(math.floor(a))
