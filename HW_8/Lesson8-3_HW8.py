# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел,
# знаходить серед них унікальне число та повертати його.
# Унікальне число - це число, яке зустрічається в списку один раз. Випадок,
### коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.

import random

## наповнюємо список рандомними цифрами від 1 до 10 :
def create_list_random(len_list, start_num, end_num) -> list[int]:           # 10=довжина списка з цисел від 1 до 5
# def create_list_random(len_list=10, start_num=1, end_num=10) -> list[int]:  # 10=довжина списка з цисел від 1 до 5
    return [random.randint(start_num, end_num) for _ in range(len_list)]     # повертає спиок 'list[int]' з 10 цифр від 1 до 5

my_random_list = create_list_random(10, 1, 10)        # змінної повертається (=) список з функції 'find_unique_value()'
print(my_random_list)               # початковий список

#####
def find_unique_values(numbers_lst: list[int]) -> list[int]:
    # # v1./ +  з використанням 'for'
    # unique_list = []
    # for ii in range(len(numbers_lst)):
    #     # num_from_list = numbers_lst[ii]
    #     # if numbers_lst.count(num_from_list) == 1:
    #     if numbers_lst.count(numbers_lst[ii]) == 1:
    #         unique_list.append(numbers_lst[ii])
    # return print(unique_list)

    # # v2. +   з використання 'while'
    # unique_list = []
    # ii = 0
    # while ii < len(numbers_lst):
    #     num_from_list = numbers_lst[ii]
    #     if numbers_lst.count(num_from_list) == 1:
    #         unique_list.append(numbers_lst[ii])
    #     ii += 1
    # return print(unique_list)

    # # v3. +
    # unique_list = []
    # for ii in numbers_lst:
    #     if numbers_lst.count(ii) == 1:
    #         unique_list.append(ii)
    # return print(unique_list)

    # v4. +  Клас!!!
    return print([ii for ii in numbers_lst if numbers_lst.count(ii) == 1])

find_unique_values(my_random_list)

