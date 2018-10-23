pharase = "Don't panic!"
plist = list(pharase)
print(pharase)
print(plist)
for nums in range (5):
    plist.pop()
plist.remove(' ')
plist.pop(0)
plist.pop(2)
plist.insert(2, ' ')
plist.insert(4, 'a')
new_pharas = ''.join(plist)
print(plist)
print(new_pharas)
