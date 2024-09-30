# Lesson 2. TASK 2
#
# Ввід числа та переведення зі 'str' в 'int' :
# user_number = int(user_number) - як варіант
user_number = int(input("Enter a 5 digit number : "))
print(user_number)
#
# Визначити всі цифри у числі можна двома шляхами (1. з використання арифмет.операцій '//' та '%' ;
# 2. з використанням функції 'divmod'):
# Вибіраю другий шлях: Використовуєм функцію 'divmod' для визначення першого цисла та залишку від ділення.
# Так робимо наступним разом із залишком поки не визнаєм всі цифри.
#
# Перша цифра :
first_number, second_number = divmod(user_number, 10000)
# print(first_number)
#
# Друга цифра :
second_number, three_number = divmod(second_number, 1000)
# print(second_number)
#
# третя цифра :
three_number, four_number = divmod(three_number, 100)
# print(three_number)
#
# Четверта і п'ята цифри :
four_number, five_number = divmod(four_number, 10)
# print(four_number)
# print(five_number)
#
# Результат (два варіанта рішення) :
print(result_number := five_number * 10000 + four_number * 1000 + three_number * 100 + second_number * 10 + first_number)
# АБО
# окремі цифри приеднуємо у зворотньому порядку, переводимо в 'int' з використання моржового оператора присваювання :
print(result_number := int(f"{five_number}{four_number}{three_number}{second_number}{first_number}"))
#
# Перевірка типа змінної :
# print(type(result_number))