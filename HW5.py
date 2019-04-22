# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

a, b, c = map(int, input('Введите через пробел верхнюю и ниюнюю границы случайного диапазона чисел '
                         'и желаемое количество: ').split())

random_numbers = [random.randint(a, b+1) for _ in range(c)]

negative_number = min(random_numbers)
negative_number_index = random_numbers.index(negative_number)

if negative_number >= 0:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Максимальный отрицательный элемент равен {negative_number} '
          f'и находиться на позиции {negative_number_index}')
