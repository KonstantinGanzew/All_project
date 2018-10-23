n = int(input())
result = set(map(str, range(1, n+1)))
while True:
    s = input()
    if s == 'HELP':
        break
    inp = set(s.split())
    if input() == 'YES':
        result.intersection_update(inp)
    else:
        result.difference_update(inp)
print(' '.join(sorted(result)))
