a = int(input())
b = int(input())
d = int(input())
even = 0
odd = 0
if a % 2 == 0:
    even += 1
else:
    odd += 1
if b % 2 == 0:
    even += 1
else:
    odd += 1
if d % 2 == 0:
    even += 1
else:
    odd += 1
if even >= 1 and odd >= 1:
    print('YES')
else:
    print('NO')
