elems = {}
fis = open('input.txt')
lst = ''
for l in fis:
    lst += l
lst = sorted(lst.split())
e, em = None, 0
for i in lst:
    elems[i] = t = elems.get(i, 0) + 1
    if t > em:
        e, em = i, t
print(e)
