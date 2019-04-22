# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

a, b, c = map(int, input('Введите через пробел верхнюю и ниюнюю границы случайного диапазона чисел '
                         'и желаемое количество: ').split())
positions_of_even_numbers = []
random_numbers = [random.randint(a, b+1) for _ in range(c)]

for el in range(len(random_numbers)):
    if not random_numbers[el] %2:
        positions_of_even_numbers.append(el)

print(f'Массив данных: {random_numbers}')
print(f'Чётные значения находятся на позициях: {positions_of_even_numbers}')
