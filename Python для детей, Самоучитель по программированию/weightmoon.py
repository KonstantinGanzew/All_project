def moon_weight_year(weight: int, plus_weight: float, age: int) -> str:
    for i in range (age):
        print(weight * 0.165)
        weight += plus_weight
