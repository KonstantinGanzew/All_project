import time

def lots_of_numbers(max = 1000) -> str:
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print('Прошло %s секунд' % (t2-t1))
