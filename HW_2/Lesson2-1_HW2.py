# Lesson 2. TASK 1
user_number = input("Enter a 4 digit number : ")
user_number = int(user_number)
print(user_number)
#
# Визначити всі цифри у числі можна двома шляхами (1. з використання арифмет.операцій '//' та '%' ;
# 2. з використанням функції 'divmod'):
# Вибіраю другий шлях: Використовуєм функцію 'divmod' для визначення першого цисла та залишку від ділення.
# Так робимо наступним разом із залишком поки не визнаєм всі цифри.
#
# Перша цифра :
first_number, second_number = divmod(user_number, 1000)
# АБО так :  first_number = user_number // 1000
print(first_number)
#
# Друга цифра :
second_number, three_number = divmod(second_number, 100)
# АБО так :  second_number = user_number % 1000 // 100
print(second_number)
#
# Третя і четверта цифри :
three_number, four_number = divmod(three_number, 10)
# АБО так :  three_number = user_number % 1000 % 100 // 10
print(three_number)
print(four_number)

