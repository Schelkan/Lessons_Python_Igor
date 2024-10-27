# Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
# Вхідні дані: Ціле число.
# Вихідні дані: Логічний тип.

from random import randint

rand_num = randint(0, 99)  # генеруємо числа 'int' для функції
def is_even(digit_num):
    if digit_num % 2 == 0:
        print(f"{digit_num} парне число")
        return True
    else:
        print(f"{digit_num} непарне число")
        return False

is_even(rand_num)

# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')