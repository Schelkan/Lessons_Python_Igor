print("Для розрахунку операції введить послідовно числа та операцію!")
number_1 = float(input("Enter first digit number : "))
# print(number_1)
math_operation = input("Enter the mathematical symbol of the operation (+, -, *, /): ")
# print(math_operation)
number_2 = float(input("Enter second digit number : "))
# print(number_2)

# # v1. Використання функції 'match'
match math_operation:
    case "+":
        print(f"{number_1}{"+"}{number_2}{"="}{number_1 + number_2}")
    case "-":
        print(f"{number_1}{"-"}{number_2}{"="}{number_1 - number_2}")
    case "*":
        print(f"{number_1}{"*"}{number_2}{"="}{number_1 * number_2}")
    case "/":
        if number_2 != 0:
            print(f"{number_1}{"/"}{number_2}{"="}{number_1 / number_2}")
        else:
            print("Дільник = 0. Повторити програму ще раз!")
    case _:              # аналог else
        print("Неправильно введено математичну операцію!")
#
#
# v2. Використання оператора 'if'
# if math_operation == "+":
#   print(f"{number_1}{"+"}{number_2}{"="}{number_1 + number_2}")
# elif math_operation == "-":
#         print(f"{number_1}{"-"}{number_2}{"="}{number_1 - number_2}")
# elif math_operation == "*":
#         print(f"{number_1}{"*"}{number_2}{"="}{number_1 * +number_2}")
# elif math_operation == "/":
#   if number_2 != 0:
#       print(f"{number_1}{"/"}{number_2}{"="}{number_1 / number_2}")
#   else:
#       print("Дільник = 0. Повторити програму ще раз!")
# else:              # аналог else
#       print("Неправильно введено математичну операцію!")



