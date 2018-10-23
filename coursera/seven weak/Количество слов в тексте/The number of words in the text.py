iin_file = open("input.txt", "r", encoding="utf8")
a = []
for i in iin_file.read().split('\n'):
    a += i.split()
print(len(set(a)))
