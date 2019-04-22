# 4. Определить, какое число в массиве встречается чаще всего.

import random

a, b, c = map(int, input('Введите через пробел верхнюю и ниюнюю границы случайного диапазона чисел '
                         'и желаемое количество: ').split())

random_numbers = [random.randint(a, b+1) for _ in range(c)]

max_count_number = 0

for el in set(random_numbers):
    current_count_number = 0
    for elem in random_numbers:
        if elem == el:
            current_count_number += 1
    if max_count_number < current_count_number:
        max_count_number = current_count_number
        number = el

print(f'Массив: {random_numbers}')
print(f'Количество числа {number} в массиве равно {max_count_number}, и число встречается чаще всего')
