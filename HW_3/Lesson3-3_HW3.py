# Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
# Тобто, в результаті повинен вийти список із 2-х списків.
# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
# Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
# у списку парна кількість елементів і в списку непарна кількість елементів.

# my_lst = [11, 12, 13, 14, 15, 16, "сімнадцать"]
my_lst = [11, 12, 13, 14, 15, 16]
# my_lst = [11]     # для перевірки
# my_lst = []       # для перевірки
# my_lst = list()   # для перевірки
print(my_lst)

length_list = len(my_lst)   # кількість елементів у списку
length_check = length_list % 2

# v1.
first_list = my_lst[:length_list // 2 + length_check]
second_list = my_lst[length_list // 2 + length_check:]
if length_list !=0:
    my_lst_2 = [first_list, second_list]
else:
    my_lst_2 = [[], []]
print(my_lst_2)

#  v2.
# if length_list !=0:
#     if length_check == 1:
#         first_list = my_lst[:length_list // 2 + length_check]
#         second_list = my_lst[length_list // 2 + length_check:]
#         my_lst_2 = [first_list, second_list]
#     else:
#         first_list = my_lst[:length_list // 2]
#         second_list = my_lst[length_list // 2:]
#         my_lst_2 = [first_list, second_list]
# else:
#     my_lst_2 = [[], []]
# print(my_lst_2)