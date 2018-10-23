a = list(map(int, input().split()))
b = []
cou = 0
for i in range(a[1]):
    b.append(int(input()))
b = sorted(b)
c = 0
for i in range(len(b)):
    if b[i] > a[0]:
        pass
    elif c >= a[0]:
        pass
    else:
        cc = c
        c += b[i]
        if c >= a[0]:
            c = cc
        else:
            cou += 1
print(cou)
