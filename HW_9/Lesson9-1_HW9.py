# На вхід функції popular_words передаються два аргументи. Текст та список слів, популярність яких необхідно визначити.
#
# При вирішенні цього завдання зверніть увагу на такі моменти
#
# Слова необхідно шукати у всіх регістрах. Тобто. якщо необхідно знайти слово "one",
# значить для нього будуть підходити слова "one", "One", "oNe", "ONE" і т.д.
# Шукані слова завжди вказані в нижньому регістрі
# Якщо слово не знайдено жодного разу, його необхідно повернути у словнику зі значенням 0 (нуль)
# Вхідні параметри: Текст і масив слів, що шукаються.
#
# Вихідні параметри: Словник, у якому ключами є шукані слова та значеннями,
# скільки разів кожнє слово зустрічаються у орігінальному тексті.

my_text0 = 'When I was One I had just begun When I was Two I was nearly new '
my_words0 = ['i', 'was', 'three', 'near']
# my_words0 = ['three', 'nearly']           # для перевірки

# 3 ВЕРСІЇ програми :

# # v1. рядок перетворюємо в список
def popular_words(text, words):
    my_text1 = text.lower().split()  # строку переводимо в ніжній регістр та створюємо список (через пробел)
    print(my_text1)

    len_words = len(words)      # кількість елементів (слів) для перевірки входжень
    dict_words = dict()         # словник пустий

    for ii in range(len_words):  # цикл по кількості слів в нашому списку

        num_count = my_text1.count(words[ii])  # кількість входжень слова в списку (строкі)
        dict_words[words[ii]] = num_count  # в словник додаємо елементи (ключ 'words[ii]' = значення 'num_count')

    print(dict_words)           # для перевірки
    return dict_words
popular_words(my_text0, my_words0)

# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')

# **************************

# # v2. якщо працюємо з рядком
# def popular_words(text, words):
#     my_text1 = text.lower()                   # строку переводимо в ніжній регістр
#     print(my_text1)
#
#     len_words = len(words)  # кількість елементів (слів) для перевірки входжень
#     dict_words = dict()  # словник пустий
#
#     for ii in range(len_words):  # цикл по кількості слів в нашому списку
#
#         num_count = my_text1.count(words[ii])  # кількість входжень слова в списку (строкі)
#
#         # якщо працюємо з рядком потрібна перевірка на повне співпадіння входження (слова):
#         # - рахуємо довжину 'words[ii]'
#         # - знаходим індех входження 'words[ii]' в строки 'my_text1'
#         # - починая з індекса, в строки 'my_text1' рахуємо довжину слова до пробелу
#         # - порівнюємо довжину 'words[ii]' з довжиною слова в 'my_text1'
#         # - якщо довжини ==, то додаємо в словник з 'num_count', інакше додаємо з 'num_count=0'
#
#         ind_word = (my_text1.find(words[ii]))  # Повертає найменший індекс, за яким виявляється початок зазначеної підрядки
#         ind_space = my_text1.find(' ', ind_word + 1)    # Пошук індексу найблищого пробелу справа
#         if ind_space-ind_word == len(words[ii]):    # перевірка довжина входження == довжинні слова в рядку
#             dict_words[words[ii]] = num_count       # якщо довжини ==, то додаємо в словник
#         else:
#             dict_words[words[ii]] = 0               # якщо довжини !=, то додаємо в словник з 'num_count=0'
#     print(dict_words)           # для перевірки
#     return dict_words
#
# popular_words(my_text0, my_words0)
#
# assert popular_words('When I was One I had just begun When I was Two I was nearly new ', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
# print('OK')

# *********************************

# # v3. Через зіпування двох списків: `words`-слова для перевірки входження, `lst_num_count`-список входжень
# def popular_words (text, words):
#
#     my_text1 = text.lower().split()         # строку переводимо в ніжній регістр та створюємо список (через пробел)
#     lst_num_count = []          # створюємо список значень 'num_count' --> lst_num_count = []
#
#     print(my_text1)
#
#     len_words = len(words)                  # кількість елементів (слів) для перевірки входжень
#     dict_words = dict()                     # словник пустий
#
#     for ii in range(len_words):             # цикл по кількості слів в нашому списку
#
#         num_count = my_text1.count(words[ii])  # кількість входжень слова в списку (строкі)
#
#         # v1.  якщо працюємо зі списком :
#         dict_words[words[ii]] = num_count  # в словник додаємо елементи (ключ 'words[ii]' = значення 'num_count')
#
#         lst_num_count.append(num_count)         # створюємо список значень 'num_count' --> lst_num_count[]
#     zipped_data = zip(words, lst_num_count)     # Зіпувати два списки
#     my_result = list(zipped_data)               # --> [('i', 4), ('was', 3), ('three', 0), ('near', 0)]
#     # print(my_result)
#     dict_words = dict(my_result)                # ---> {'i': 4, 'was': 3, 'three': 0, 'near': 0}
#
#     print(dict_words)           # для перевірки
#     return dict_words
#
# popular_words(my_text0, my_words0)
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')

