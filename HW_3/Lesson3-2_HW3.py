# перенести останній елемент списку з кінця на початок
my_lst = [11, 12, 13, 14, 15, "Переміщення"]
# my_lst = [11]     # для перевірки
# my_lst = []       # для перевірки
# my_lst = list()   # для перевірки
print(my_lst)

length_list = len(my_lst)   # кількість елементів у списку
# print(length_list)

# перевірка кількості елементів (повинно бути > 1)
if length_list > 1:                             # варіант 1
# if length_list != 0 and length_list != 1:     # варіант 2
    end_first_el = my_lst[-1]      # останній елемент у списку
    # print(end_first_el)

    # my_lst.remove(end_first_el)     # видалення останього елементу по значенню
    del_end = my_lst.pop(length_list-1)      # змінна = видалення останього елементу по індексу

    my_lst.insert(0, end_first_el)
    print(my_lst)
else:
    print(f"{"Кількість елементів у списку = "}{length_list}{".  Переміщення елементів не можливо!"}")

