cP = int(input())
resPer = []
for i in range(cP):
    resPer.append(list(input().split()))
for i in resPer:
    i[1] = int(i[1])
resPer.sort(key=lambda x: -x[1])
for i in resPer:
    print(i[0])
