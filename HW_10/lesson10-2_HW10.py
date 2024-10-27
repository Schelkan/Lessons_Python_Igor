# Напишіть функцію first_word, яка у переданому рядку знайде її перше слово.
# При розв'язанні задачі зверніть увагу на наступні моменти:
# У рядку можуть зустрічаються крапки та/або коми
# Рядок може починатися з літери або, наприклад, з пробілу або точки
# У слові може бути апостроф і він є частиною слова
# Весь текст може бути представлений лише одним словом та все
# Вхідні параметри: Рядок.
# Вихідні параметри: Рядок

"""
Виконання.
Видаляємо з рядка всі зайві символи (замінюємо на ' ')
Шукаємо перше слово до пробелу або кінця рядку
По циклу перевіряємо всі символи на літеру або "'" . Якщо False, шукаємо наступне слово по пробелам.
"""


my_str = "don't. touch, - it"       # ТИМЧАСОВА строка для перевірки
# my_str = "Hello world"
# my_str = "greetings, friends"
# my_str = "don't touch it"
# my_str = ".., and so on ..."
# my_str = "hi"
# my_str = "Hello.World"
#
# v1. Згідно завдання
def first_word(str_user0):
    # створюємо строки для пошуку слова:
    str_user1 = str_user0.replace(".", " ").replace(",", " ").replace("-", " ").strip()+" "

    ind_space = str_user1.find(" ")             # Пошук індексу найблищого пробелу справа

    my_word = str_user1[:ind_space]             # слово (потребує перевірки на відсутність зайвих символів)
    # print(my_word)      # для перевірки
    return my_word


# first_word(my_str)

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

