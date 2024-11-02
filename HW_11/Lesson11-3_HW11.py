# Завдання ускладнюється.
# Ваша функція is_even, як і раніше, повинна повертати True якщо число парне,
# або False якщо число непарне, але при цьому НЕ МОЖНА використовувати ділення у функції, та дії пов'язані з ним.
# Тобто. заборонено використовувати:  /, //, % та divmod
# Складність ще полягає і в тому, щоб знайти рішення, яке не залежало б від розміру числа :)
#
# Вхідні дані: Ціле число.
# Вихідні дані: True або False


# v1.
# def is_even(number):
#     # num_even = '02468'
#     # Перетворюємо число на рядок і перевіряємо останню цифру
#     # end_digit = str(number)[-1]
#     len_num = len(str(number))
#     end_digit = str(number)[len_num-1]
#     print(end_digit)                        # для перевірки
#     if end_digit in num_even:
#         return True
#     else:
#         return False

# v2.
# def is_even(number):
#     # Перетворюємо число на рядок і перевіряємо останню цифру
#     end_digit = str(number)[len(str(number)) - 1]       #вибираємо останню цифру
#     print(end_digit)                                    # для перевірки
#     if end_digit in '02468':
#         return True
#     else:
#         return False

# v3.
def is_even(number):
    # Перетворюємо число на рядок і перевіряємо останню цифру
    end_digit = str(number)[len(str(number)) - 1]       #вибираємо останню цифру
    # print(end_digit)                                    # для перевірки
    return end_digit in '02468'                        # якщо парна цифра, 'return' повертає True, інакше False

    # Якщо остання цифра є однією з парних цифр, повертаємо True
    # return last_digit in '02468'

# is_even(6464)     # для перевірки

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')