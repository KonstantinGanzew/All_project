a = int(input()) - 1
b = 1
c = 1
d = str(c) + ' '
while True:
    if c < a:
        b += 1
        c = b**2
        d += str(c)
    else:
        break
    d += ' '
print(d[0:-1])
