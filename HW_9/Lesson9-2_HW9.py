# Є набір чисел (float або int). Вам потрібно знайти різницю між найбільшим (максимум) і найменшим (мінімум) елементом.
# Ваша функція difference має вміти працювати з невизначеною кількістю аргументів.
# Якщо аргументів немає, то функція повертає 0 (нуль).
# Якщо з 3-м тестом будуть проблеми, використовуйте функцію округлення round(x, 2), де х це число, яке потрібно округлити.
#
# Вх. Дані: Змінна кількість аргументів як числа (int, float).
# Вих. Дані: Різниця між максимумом і мінімумом як число (int, float).

import random
# # from random import *
# from random import randint

list_args = []
# створюємо рандомний список з рандомною кількістю елементів (1:10) для передачі в функцію :
for i in range(random.randint(1, 10)):          # створюємо рандомний список з рандомною кількістю елементів
    jj = random.randint(0, 99)                  # генеруємо числа 'int'
    # jj = random.random()                              # генеруємо числа 'float'
    list_args.append(jj)
print(list_args)


# def difference(*dif_num):         # якщо вказати декілька елементів
def difference(dif_num):
   if dif_num == ():                # якщо список пустий - для функції 'def difference(*dif_num)'
       return 0
   elif len(dif_num) == 1:          # якщо список має один елемент
       print(dif_num[0])            # для перевірки
       return dif_num[0]
   else:
       rezult = round((max(dif_num)-min(dif_num)), 2)
       print(rezult)                # для перевірки
       return rezult

difference(list_args)

# ==================
# тільки для функції (див.вище): `def difference(*dif_num)`
# difference(1, 2, 3)
# difference(5, -5)
# difference(10.2, -2.2, 0, 1.1, 0.5)
# difference()

# перевірка тільки для функції : `def difference(*dif_num)`
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')