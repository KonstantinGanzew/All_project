a = int(input())
b = int(input())
count = 1
while a < b:
    count += 1
    c = a / 100 * 10
    a += c
print(count)
