import random

money = random.randint(0, 5000)
if money > 100 and money < 500:
    print('Маловато будет')
elif money > 1000 and money < 5000:
    print('Денег много не бывает')
else:
    print('И так и сяк')

print(money)
