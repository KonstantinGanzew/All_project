print(
    0 in (map(
        int,
        open('input.txt', 'r', encoding='utf8').read().split())
    )
)
