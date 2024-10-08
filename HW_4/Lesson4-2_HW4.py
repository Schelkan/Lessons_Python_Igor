# Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд],
# потім перемножити цю суму на останній елемент вхідного масиву.
# Для порожнього масиву результат завжди 0

# Приклади списків :
# my_list0 = [3, 1, 5, 7, 4, 10, 11, 54, 4]
my_list0 = [0, 1, 7, 2, 4, 8]
# my_list0 = [8]
# my_list0 = []
print(my_list0)

my_list1 = my_list0[::2]                # кожний друге значення списку my_list0 -> в новий список my_list1
print(my_list1)
list1_length = len(my_list1)            # довжина списку

if list1_length == 0:                   # якщо список пустий
    number_end = 0                      # останній елемент у списку відсутній
    print("Список пустий.")
else:                                   # якщо список не пустий
    number_end = my_list0[-1]           # останній елемент у списку
    sum_number = my_list1[0]            # перший елемент у списку
    print("(", sum_number, end=" ")     # починаємо збірати строку ...
    i = 1
    while i < list1_length:                 # цикл - складаємо всі елементи списку
        sum_number = sum_number + my_list1[i]
        print("+", my_list1[i], end=" ")    # збіраємо строку ...
        i += 1
    print(f"{") * "}{number_end}{" = "}{sum_number * number_end}")       # РЕЗУЛЬТАТ завдання
