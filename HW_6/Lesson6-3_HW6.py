# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.

# user_number0 = input("Введить число для обробки > 9 : ")
user_str0 = input("Введить число для обробки : ")
# print(user_str)
ii_num = int(user_str0)

if ii_num <= 9:
    print("Ви ввели число <= 9 !")

while ii_num > 9:                           # цикл поки результат не буде <= 9
    # len_num = len(user_str0)
    user_str0 = str(ii_num)                 # нове значення після перемноження - str()
    i = 0
    user_number1 = 1                        # змінна для створення нового числа після перемноження цифр
    # str_num =[]                           # пустий список для кожної цифри в числі - як варіант 2 зробити через список
    for i in range(len(user_str0)):         # цикл по визначенню кожної цифри та їх перемноження - нове число
        # str_num.append(user_str0[i])      # створення списку, але так довже і не зручно
        user_number1 = user_number1 * int(user_str0[i])
        # print(user_number1)
    ii_num = user_number1
print(ii_num)








