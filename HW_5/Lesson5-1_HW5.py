# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation, string.digits), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import keyword
import string
symb_err = string.punctuation + string.digits           # string.ascii_letters
word_err = keyword.kwlist

str_user = input("Введить слово : ")
str_user = str_user.strip()                     # забирає з кінців зайви пробели на всяк випадок

#  Первірка вимог:
if str_user in word_err:                        # якщо введене слово входить до списку зареєстрованих слів
    print("False")
elif str_user.count("_") > 1:                   # не більш чим з одного нижнього підкреслення "_"
    print("False")
# elif str_user[0] in string.digits:              # v1. якщо починається з цифри
    # print("False")
elif str_user[0].isnumeric():                   # v2. якщо починається з цифри
    print("False")
elif str_user.islower():                        # якщо рядок складається лише із символів у нижньому регістрі
    print("True")
else:                                           # входить до списку зареєстрованих слів або велика літера
    print("False")

