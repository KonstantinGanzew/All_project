fin = open('input.txt')
line = ''
for l in fin:
    line += l
counter = {}
for word in line.split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
