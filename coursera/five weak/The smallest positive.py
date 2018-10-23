a = list(map(int, input().split()))
m = 0
c = 0
for i in a:
    if i > 0 and c == 0:
        m = i
        c += 1
    else:
        if 0 < i < m:
            m = i
print(m)
