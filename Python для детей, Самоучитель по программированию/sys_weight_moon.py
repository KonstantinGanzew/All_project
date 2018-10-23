def moon_weight_sys() ->str:
    weight = int(input('Введите вес по умолчанию: '))
    plus_weight = float(input('Введите вес на которй вы будете поправляться: '))
    year = int(input('Введите количество лет: '))
    for i in range (year):
        print(weight * 0.165)
        weight += plus_weight
