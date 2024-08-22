a = 'СЛОВАРЬ'
print(a)
my_dict = {'Мира': 1985, 'Слава': 1997, 'Рита': 2003}
print(my_dict)
print(my_dict.get('Слава'))
print('отсутствующее значение:', my_dict.get('Алина'))
my_dict.update({'Максим': 1987, 'Артур': 2015})
print(my_dict)
removed_year = my_dict.pop('Максим')
print(removed_year)
print(my_dict)
b = 'МНОЖЕСТВА'
print(b)
my_set = {1, 2, 3, 4, 3, 4, 6, 2, 5, False, True, 'Urban', 'уроки', (1,3,5)}
print(my_set)
my_set.add(65.789)
my_set.add('string')
my_set.discard(4)
print(my_set)
