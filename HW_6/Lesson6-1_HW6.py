# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import string
str_symb = string.ascii_lowercase + string.ascii_uppercase           # string.ascii_letters
print(str_symb)
str_user0 = input("Введить строку у форматі < літера-літера > : ")

# можна зробити перевірку на ввод тільки літерів зі строки (англ.літери)
# можна зробити перевірку на кількість символів в строці - повинно бути 3
# можна зробити перевірку на літери в першой і третьої позиції, друга позиція повинна бути '-'

ind_symb1 = str_symb.index(str_user0[0])    # індекс літери в строкі 'str_symb'
ind_symb2 = str_symb.index(str_user0[2])

# v1. Варіант коротший
if str_symb.index(str_user0[0]) == str_symb.index(str_user0[2]):
# if str_user0[0] == str_user0[2]:
    print(str_user0[0])
else:
    # print(str_symb[ind_symb1:ind_symb2 + 1])          # якщо без умови перевірки на вводні літери
    if ind_symb1 < ind_symb2:
        print(str_symb[ind_symb1:ind_symb2 + 1])
    else:
        # print(str_symb[ind_symb2:ind_symb1 + 1])      #
        str_symb2 = str_symb[ind_symb2:ind_symb1 + 1]   # можна вивести в зворотньому порядку
        print(str_symb2[::-1])

# # v2. Варіант більш довгий
# if ind_symb1 < ind_symb2:        # перевірка як будувати строку з меньшого до більшого або навпаки
#     i1 = 0
#     i2 = 1
# else:                                   # будувати строку з більшого до меньшого
#     i1 = 1
#     i2 = 0
#
# if str_symb.index(str_user0[0]) == str_symb.index(str_user0[2]):
# # if str_user0[0] == str_user0[2]:
#     print(str_user0[0])
# else:
#     # print(str_symb[ind_symb1:ind_symb2 + 1])      # якщо без умови перевірки на вводні літери
#     if i1 < i2:
#         print(str_symb[ind_symb1:ind_symb2 + 1])
#     else:
#         # print(str_symb[ind_symb2:ind_symb1 + 1])
#         str_symb2 = str_symb[ind_symb2:ind_symb1 + 1]   # можна вивести в зворотньому порядку
#         print(str_symb2[::-1])