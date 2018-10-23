a = int(input())
c = 1
b = True
if -1 <= a <= 1:
    print(a)
    b = False
while b:
    c += 1
    if a % c == 0:
        print(c)
        b = False
