# Напишіть функцію-генератор prime_generator, яка повертатиме прості числа.
# Верхня межа цього діапазону визначається параметром цієї функції.
# Наприклад, виклик функції :
# list(prime_generator(10)) повинен відповідати послідовності з чисел [2, 3, 5, 7] .
# Наступне число в цій послідовності - 11 і воно більше 10 тому воно не потрапляє в цей ряд


lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def prime_generator(end):
    def is_prime(num1):                 # num0
        # print(num1)
        if num1 <= end and lst.count(num1):     # якщо число меньш вказаного і є в списку, то True (вибираємо)
            # print(num1)                       # для перевірки
            return True
        else: return False
        return True

    for num0 in range(end+1):            # генератор від 1 до 'end+1' ('end+1' - не включно)
        if is_prime(num0):               # якщо повертається 'True', то
            yield num0                   # наступне число


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

import random


#  ПРИКЛАД генератора:
# def generate_random_list(list_len, start_value=1, end_value=100):
#     # v1
#     # nums = []
#     # for i in range(list_len):
#     #     nums.append(random.randint(start_value, end_value))
#     #
#     # return nums
#
#     # v2
#     return [random.randint(start_value, end_value) for _ in range(list_len)]

