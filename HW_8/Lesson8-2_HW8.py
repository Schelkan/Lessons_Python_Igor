# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво
# без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False

# Приклади строк паліндромів :
# my_line0 = "А роза упала на лапу Азора"
my_line0 = 'A man, a plan, a canal: Panama'
# my_line0 = '0P'
# my_line0 = 'a.'
# my_line0 = 'aurora'

import string
symb_err = string.punctuation       # + string.digits  # string.ascii_letters

def is_palindrome(my_line):
    # my_line = my_line.strip()             # забирає з кінців зайви пробели на всяк випадок
    my_line = my_line.lower()               # переводимо в ніжній регістр
    my_line = my_line.replace(" ", "")      # видаляє пробели, заміняя їх на ""
    len_line = len(my_line)

    # Формуємо першу та реверсну строки :

    # v1. через строку
    line_new = ""
    for ii in range(len_line):
        if not (my_line[ii] in string.punctuation):
            line_new = line_new + my_line[ii]
    line_rev = line_new[::-1]               # метод - срез строки

    # # v2. через список
    # line_new = []
    # for ii in range(len_line):
    #     if not (my_line[ii] in string.punctuation):
    #         line_new.append(my_line[ii])
    # line_rev = line_new.copy()
    # line_rev.reverse()                    # Перебудовує елементи списку у зворотному порядку.
    #
    # line_rev = "".join(line_rev)          # зі списку будує строку
    # line_new = "".join(line_new)

    # print(line_new)                       # для перевірки строк
    # print(line_rev)

    # перевірка строки, що вона паліндром :
    if line_new == line_rev: return print(True)     # для перевірки 'assert' треба змінити на 'return True'
    else: return print(False)                       # для перевірки 'assert' треба змінити на 'return False'

is_palindrome(my_line0)

# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")
