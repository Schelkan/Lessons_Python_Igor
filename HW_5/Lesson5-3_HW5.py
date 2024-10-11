# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag. -> #........
# Декілька правил:
# ніяких символів з набору string.punctuation та string.digits не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string
lst_err = string.punctuation + string.digits
# print(lst_err)
string_input = input("Введить строку для hashtag: ")
string_input = string_input.strip()     # забирає з кінців зайви пробели на всяк випадок
# print(string_input)
len_str = len(string_input)             # загальна довжина введенноъ строки

# Розбиття рядка на підрядки (по замовченню за пробілом)
string_many = string_input.split(" ", -1)
# print(string_many)
len_str_many = len(string_many)         # кількість підрядків
# print(len_str_many)
string_new = []

i = 0  # рахуємо підрядки в рядку - працюємо з кожним підрядком окремо, але можна одразу з рядком повністю
while i < len_str_many:           # робота окремо з кожним підрядком; можна використати: for i in range(len_str_many)
    if string_many[i].isalpha():                    # якщо підрядок з літерів, його не перевіряємо
        string_many[i] = string_many[i].title()     # для підрядків робимо перши заглавни літери
        # print(string_many[i])                     # для перевірки
        string_new.append(string_many[i])

    else:
        str_temp0 = string_many[i]                   # тимчасовий рядок
        str_temp1 = []
        # print(str_temp0)
        ii = 0
        for ii in range(len(str_temp0)):

            if not (str_temp0[ii] in lst_err):      # цикл перевірки кожного символа в підрядку
                str_temp1.append(str_temp0[ii])     # додавання в строку якщо літера
                ii += 1
            else:
                # # str_temp1.append(str_temp0[ii])
                ii += 1

        # str_temp2 = "".join(str_temp1)            # об'єднуєм літери
        # str_temp2 = str_temp2.title()             # перша заглавна
        # string_new.append(str_temp2)
            # або однієї строкою :
        string_new.append("".join(str_temp1).title())       # додаємо до нового загального списку

    i += 1

lst_hashtag = "#" + "".join(string_new)             # зібраний хештег

if len(lst_hashtag) > 140:                          # перевірка на довжину і вивід на екран
    our_hashtag = lst_hashtag[:140]
else:
    our_hashtag = lst_hashtag
print(f"{"Фінішний хештег: "}{our_hashtag}")