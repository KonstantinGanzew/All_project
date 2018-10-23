a = int(input())
maxA = 0
maxB = 0
while a != 0:
    if maxA <= a:
        maxB = maxA
        maxA = a
    else:
        if maxB <= a <= maxA:
            maxB = a
    a = int(input())
print(maxB)
