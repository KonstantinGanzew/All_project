import random

ninjas = random.randint(0, 50)

if ninjas < 50 and ninjas > 30:
    print('Их слишком много')
elif ninjas < 30 and ninjas > 10:
    print('Будет непросто, но я с ними разделаюсь')
else:
    print('Я одолею этих ниндзя')

print(ninjas)
