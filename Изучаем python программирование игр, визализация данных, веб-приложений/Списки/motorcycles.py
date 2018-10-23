motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Изменили значение 1 элемента с списке

motorcycles[0] = 'ducati'
print(motorcycles)

#Добавили в конец списка навый элемент

motorcycles.append('honda')
print(motorcycles)

#Добавили 3 элемента в список

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Добавили элемент 'ducation' на первую позицую в список

motorcycles.insert(0, 'ducati')
print(motorcycles)

#Удалили 1 элемент из списка, без возврата

del motorcycles[0]
print(motorcycles)
motorcycles.insert(0, 'ducati')

#Удаление последнего элемента с возможностью врнуть

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Удаление последнего и первого элемента в возможностью вернуть

motorcycles.append(popped_motorcycle)
last_owned = motorcycles.pop()
print('The last motorcycle I owned was a %s' % last_owned)
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a %s' % first_owned)

#Удаление из списка элемента по значению

motorcycles.insert(0, first_owned)
motorcycles.append(last_owned)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.insert(2, 'ducati')

#Удаление из списка элемента по значению с возможностью вернуть

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA' + too_expensive.title() + ' is too expensive for me.')

