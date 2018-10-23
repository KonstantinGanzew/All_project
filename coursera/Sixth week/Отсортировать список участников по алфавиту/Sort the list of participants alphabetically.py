fileList = []
inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
for line in inFile:
    fileList.append(line.split())
fileList.sort(key=lambda x: x[0])
fl = []
for line in fileList:
    fl.append(line[0] + ' ' + line[1] + ' ' + line[3] + '\n')
for l in fl:
    outFile.write(l)
inFile.close()
outFile.close()
