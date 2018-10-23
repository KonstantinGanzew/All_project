n = int(input())
i = n % 10
if 10 < n < 20 or i == 0 or (i >= 5 and i <= 9):
    print(str(n), 'korov')
elif i == 1:
    print(str(n), 'korova')
else:
    print(str(n), 'korovy')
