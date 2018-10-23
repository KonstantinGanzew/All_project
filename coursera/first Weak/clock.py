a = int(input())
h = (a // 3600) % 24
m = (a // 60) % 60
mm = str(m // 10) + str(m % 10)
s = (a % 3600) % 60
ss = str(s // 10) + str(s % 10)
print(h, mm, ss, sep=':')
