def cor(lis):
    a = []
    aa = 1
    for i in range(len(lis)):
        b = (aa, lis[i])
        a.append(tuple(b))
        aa += 1
    return a


def nearest(lst, b):
    if lst < b[0][1]:
        return b[0][0]
    elif lst > b[-1][1]:
        return b[-1][0]
    else:
        for i in range(len(b)):
            if lst < b[i][1]:
                if abs(lst - b[i][1]) > abs(lst - b[i - 1][1]):
                    return b[i - 1][0]
                else:
                    return b[i][0]

a = int(input())
aa = tuple(map(int, input().split()))
b = int(input())
bb = tuple(map(int, input().split()))
bb = cor(bb)
bb.sort(key=lambda x: x[1])
for i in aa:
    print(nearest(i, bb), end=' ')
