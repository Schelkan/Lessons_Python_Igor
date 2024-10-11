# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.
#
while True:
    print("Для розрахунку операції введить послідовно числа та операцію!")
    number_1 = float(input("Enter first digit number : "))
    math_operation = input("Enter the mathematical symbol of the operation (+, -, *, /): ")
    number_2 = float(input("Enter second digit number : "))

    # # v1. Використання функції 'match'
    match math_operation:
        case "+":
            print(f"{number_1}{"+"}{number_2}{"="}{number_1 + number_2}")
        case "-":
            print(f"{number_1}{"-"}{number_2}{"="}{number_1 - number_2}")
        case "*":
            print(f"{number_1}{"*"}{number_2}{"="}{number_1 * +number_2}")
        case "/":
            if number_2 != 0:
                print(f"{number_1}{"/"}{number_2}{"="}{number_1 / number_2}")
            else:
                print("Дільник = 0. Повторити програму ще раз!")
        case _:              # аналог else
            print("Неправильно введено математичну операцію!")

    print("Розрахунок виконаний!")
    calc = input("Для продовження/закінчення роботи калькулятора натисніть клавішу: y / n :")

    # # v1.
    if calc == "y" or calc == "Y":
        print()
        continue
    else:
        break

    # # v2.
    # match calc:
    #     case "y":
    #         continue
    #     case "Y":
    #         continue
    #     case "n":
    #         break
    #     case "N":
    #         break
    #     case _:
    #         break
