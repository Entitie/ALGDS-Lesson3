# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a, b, c = map(int, input('Введите через пробел верхнюю и ниюнюю границы случайного диапазона чисел '
                         'и желаемое количество: ').split())

random_numbers = [random.randint(a, b+1) for _ in range(c)]

max_number = max(random_numbers)
min_number = min(random_numbers)

max_index = random_numbers.index(max_number)
min_index = random_numbers.index(min_number)

print(f'Был список такой: {random_numbers}')

random_numbers[max_index], random_numbers[min_index] = random_numbers[min_index], random_numbers[max_index]

print(f'А стали списокй вот такой: {random_numbers}')
