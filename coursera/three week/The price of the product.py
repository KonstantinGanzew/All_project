import math
a = float(input())
b = math.floor(a)
c = float('{0:.2f}'.format(a % b)) * 100
print(b, int(c))
