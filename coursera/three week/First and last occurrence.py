s = input()
j = s.find('f')
i = s.rfind('f')
if j == -1 and i == -1:
    pass
elif j >= 0 and i >= 0:
    if j != i:
        print(j, i)
    else:
        print(j)
