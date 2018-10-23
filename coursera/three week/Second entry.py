s = input()
a = s.find('f')
if a == -1:
    print('-2')
else:
    b = s.find('f', a + 1)
    if b == -1:
        print('-1')
    else:
        print(b)
