import random

twinkies = random.randint(0, 1000)
if twinkies < 100:
    print('Слишком мало')
elif twinkies > 500:
    print('Слишком много')
else:
    print('ЗБС')

print(twinkies)
