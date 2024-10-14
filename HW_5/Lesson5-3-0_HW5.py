# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag. -> #........
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string
# print(string.punctuation)
lst_err = string.punctuation
print(lst_err)
string_input = input("Введить строку для hashtag: ")
string_input = string_input.strip()     # забирає з кінців зайви пробели
# print(string_input)
len_str = len(string_input)             # загальна довжина введенноъ строки

# Розбиття рядка на підрядки (по замовченню за пробілом)
string_many = string_input.split(" ", -1)
# print(string_many)
len_str_many = len(string_many)         # кількість підрядків


i = 0                           # рахуємо підрядки в рядку
while i < len_str_many:        # робота окремо з кожним підрядком; можна використати: for i in range(len_str_many)
        if string_many[i].isalpha():                    # якщо підрядок з літерів, його не перевіряємо
            string_many[i] = string_many[i].title()     # для підрядків робимо перши заглавни літери
            # print(string_many[i])                     # для перевірки
            i += 1
        else:
            string_symbol0 = string_many[i]             # нова змінна для підрядку [i]
            string_symbol1 = []                         # зміна для створення нового підрядку з літерів
            ii = 0
            for ii in range(len(string_symbol0)):       # цикл перебору всіх символів в підрядку (по довжині підрядку)
                # якщо символ є літерою, то створюємо новую підстроку

                # string_symbol1 = []                     # зміна для створення нового підрядку з літерів
                symbol_str = 0                          # індекс символів в підрядку

                # if type(string_symbol[symbol_str]) = str():                      # перевірка символа на str()
                while symbol_str < len(string_symbol0):
                    if isinstance(string_symbol0[symbol_str], str):                 # перевірка символа на str()
                        print(string_symbol0[symbol_str])
                        # string_symbol1 = (
                        string_symbol1.append(string_symbol0[symbol_str])     # збіраємо новий підрядок
                        print(string_symbol1)
                        symbol_str += 1                 # наступний символ в підрядку
                        # ii += 1
                    else:
                        # якщо не символ, то не додаємо до нового підрядку
                        symbol_str += 1                 # наступний символ в підрядку
                        # string_many[i].
                        # symbol_str =
                ii += 1
            string_many[i].replace(string_symbol1)
            i += 1

            # string_many[i] = string_many[i].strip()

            # string_many[i] = string_symbol1.title()          # string_many[i] = string_many[i].title()
            # print(string_many[i])
            # print("False")



print(string_many)

# **************************************
# i = 0
# string_out = []
# while i < len_str:
#     print(string_input[i])
#
#     string_out.append(string_input[i])      # додає кожний символ в новий список
#     i += 1
#     print(string_out)


# ***************************************

#
#     qq = ""
#     num_str = 0
#     for
#     if string_input[num_str] == str()
#
#
#     ii = 0

# sentence = "Hello, world"
# for letter in sentence:
#     if litter.str():
#         print(letter, end=" ")
#     # else:
#         # print(f"Не літера:"{litter})


# print(string.punctuation)

# Розбиття рядка на підрядки (по замовченню за пробілом)
# my_string = "I like   Python"
# lst = my_string.split()
# print(lst) # виведе: ['I', 'like', 'Python']
# або
# my_string = "I like Python"
# lst = my_string.split('i')
# print(lst) # виведе: ['I l', 'ke Python']

# title() Першу літеру кожного слова переводить у верхній регістр, а решта в нижній
# my_string = "i like python"
# my_string = my_string.title()
# print(my_string)  # виведе: I Like Python

# isalpha() перевіряє, чи рядок складається лише з літер
# my_string = "Beautiful is better than ugly"
# # є символи, які не є літерами (пробіл)
# print(my_string.isalpha()) # виведе:  False
# # або
# my_string = "Beautiful"
# print(my_string.isalpha()) # виведе: True

# join() Повертає рядок, зібраний з елементів зазначеного об'єкта, що підтримує ітерування (список, рядок, тощо)
# my_lst = ['I', 'like', 'Python']
# # пробіл, як символ для з'єднання елементів зі списку
# _string = " ".join(my_lst)
# print(_string) # виведе: I like Python
