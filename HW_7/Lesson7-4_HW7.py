# Напишіть функцію common_elements, яка згенерує два списки елементів
# з генераторного виразу (range) для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.

# # v1. Згідно завданню:
set_list_3 = set()              # пуста множина для чисел кратних 3
set_list_5 = set()              # пуста множина для чисел кратних 5
def common_elements():
    for i in range(1, 101):     # цикл від 1 до 100
        if i % 3 == 0:              # по циклу створюємо множину для чисел кратних 3
            set_list_3.add(i)           # додаємо елемент в множину
        if i % 5 == 0:              # по циклу створюємо множину для чисел кратних 5
            set_list_5.add(i)           # додаємо елемент в множину
        i += 1
    list_12 = set_list_3.intersection(set_list_5)    # перетин множин (що загальне у першої множини з другим)
    print(list_12)
    return list_12
common_elements()
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


# ************************************************
# # v2. Версія відрізняється від постановки задачі, але результат той же - функція виконує тільки перетин
# #     Можна одразу створювати множини, а можна створювати списки - потім в множини
# # my_list_3 = []              # пустий списко для чисел кратних 3
# # my_list_5 = []              # пустий списко для чисел кратних 5
# set_list_3 = set()              # пуста множина для чисел кратних 3
# set_list_5 = set()              # пуста множина для чисел кратних 5
#
# for i in range(1, 101):     #
#     if i % 3 == 0:              # по циклу створюємо 'перелік' чисел кратних 3
#         # my_list_3.append(i)       # якщо через списки
#         set_list_3.add(i)           # якщо через множини
#     if i % 5 == 0:              # по циклу створюємо 'перелік' чисел кратних 5
#         # my_list_5.append(i)       # якщо через списки
#         set_list_5.add(i)           # якщо через множини
#     i += 1
# # set_list_3 = set(my_list_3)       # список в множину
# # set_list_5 = set(my_list_5)       # список в множину
#
# def common_elements(list_1, list_2):
#     list_12 = list_1.intersection(list_2)    # перетин множин (що загальне у першої множини з другим)
#     print(list_12)
#     return list_12
# common_elements(set_list_3, set_list_5)
# # assert common_elements(set_list_3, set_list_5) == {0, 75, 45, 15, 90, 60, 30}


# ************************************************
# # v3. Версія відрізняється від постановки задачі - робота тільки зі списком, але результат той же :)
# my_list_35 = []                 # пустий списко чисел кратних 3 і 5
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 ==0:
#         my_list_35.append(i)
#     i += 1
# print(my_list_35)

