a = int(input())
max = 0
count = 1
while a != 0:
    if max == a:
        count += 1
    if max < a:
        max = a
        count = 1
    a = int(input())
print(count)
