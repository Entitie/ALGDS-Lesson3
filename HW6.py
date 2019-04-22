# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a, b, c = map(int, input('Введите через пробел верхнюю и ниюнюю границы случайного диапазона чисел '
                         'и желаемое количество: ').split())

random_numbers = [random.randint(a, b+1) for _ in range(c)]

max_number = max(random_numbers)
min_number = min(random_numbers)

max_index = random_numbers.index(max_number)
min_index = random_numbers.index(min_number)

if min_index > max_index:
    max_index, min_index = min_index, max_index

sum_of_elem = 0

for el in range(min_index + 1, max_index):
    sum_of_elem += random_numbers[el]

print(f'Левая граница {min_number} позиция {min_index}')
print(f'Правая граница {max_number} позиция {max_index}')
print(f'Массив: {random_numbers}')
print(f'Сумма элементов между минимальным и максимальным равна {sum_of_elem}')
