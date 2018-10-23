a = list(map(int, input().split()))
m = None
c = 0
for i in a:
    if c == 0:
        m = i
        c += 1
    else:
        if i > m:
            print(i, end=' ')
        m = i
