# Написати функцію say_hi, яка представить людину за переданими параметрами.
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int)
# Функція має повернути рядок.

# # v1. без циклу на перевірку вхідних даних
# #
# user_name0 = input("Enter your name: ")
# user_age0 = input("Enter your age: ")
#
# # user_name0 = user_name0.strip()                 # забирає пробели (по замовченню) з обох кінців
# # user_name1 = user_name0.replace(" ", "")          # видаляємо всі пробели
#
# # перевірка на введення літерів для 'user_name'
# if not user_name0.replace(" ", "").isalpha():
#     print("Error your name!")
# user_name0 = user_name0.title()                     # кожне слово з великої літери
#
# # # перевірка на введення числа для 'user_age'
# if not user_age0.isdigit():
#     print("Error your age!")
#
# def say_hi(name: str, age: int):
#     print(f"Hi! My name is {name} and I`m {age} years old.")
#     # return f"Hi! My name is {name} and I`m {age} years old."
#
# say_hi(user_name0, user_age0)
# # assert say_hi("Alex", 32) == "Hi! My name is Alex and I`m 32 years old.", `Test1`


# ************************************************

# v2. з перевіркою вхідних даних з використанням циклу 'while'
#
ii, jj = 0, 0
# while not user_name0.replace(" ", "").isalpha() or user_age0.isdigit():
while ii == 0 or jj == 0:
    ii, jj = 0, 0
    user_name0 = input("Enter your name: ")
    user_age0 = input("Enter your age: ")
    user_name0 = user_name0.strip()         # забирає з кінців зайви пробели - на всяк випадок
    user_age0 = user_age0.strip()           # забирає з кінців зайви пробели - на всяк випадок

    # перевірка на введення літерів для 'user_name'
    if not user_name0.replace(" ", "").isalpha():
        print("Error your name!")
        ii = 0
    else: ii = 1
    # print(ii)             # для перевірки
    user_name0 = user_name0.title()         # кожне слово з великої літери

    # # перевірка на введення числа для 'user_age'
    if not user_age0.isdigit():
        print("Error your age!")
        jj = 0
    else: jj = 1
    # print(jj)             # для перевірки
def say_hi(name: str, age: int):
    print(f"Hi! My name is {name} and I`m {age} years old.")
    return f"Hi! My name is {name} and I`m {age} years old."

say_hi(user_name0, int(user_age0))
# assert say_hi("Alex", 32) == "Hi! My name is Alex and I`m 32 years old.", `Test1`
