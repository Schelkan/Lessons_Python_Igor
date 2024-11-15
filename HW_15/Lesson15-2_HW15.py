# Створіть клас «Правильний дріб» та реалізуйте методи порівняння, додавання, віднімання та множення
# для екземплярів цього класу.
#
# https://www.google.com/search?q=Правильний+дріб
"""
    методи для реалізації операторів порівняння:
    __eq__() – для равенства `==`
    __ne__() – для неравенства `!=`
    __lt__() – для оператора меньше `<`
    __le__() – для оператора меньше или равно `<=`
    __gt__() – для оператора больше `>`
    __ge__() – для оператора больше или равно `>=`

    методи для реалізації арифметичних операторів:
    __add__() – для операции сложения `+`
    __sub__() – для операции вычитания `-`
    __mul__() – для операции умножения `*`
    __truediv__() – для операции деления `/`
    ...

"""

# from math import gcd
import math

class Fraction:

    def __init__(self, numer, denom):
        self.numer = numer              # чисельник (numerator)
        self.denom = denom              # знаменник (denominator)
        if self.denom == 0:
            # print("Знменник рівняється 0 - на 0 ділити не можна!")
            raise ValueError("Знменник рівняється 0 - на 0 ділити не можна!")
        elif self.numer >= self.denom:
            print("Дріб не є 'Правильний дріб' : чисельник = " + str(self.numer) + " > знаменник = " + str(self.denom))

    def __mul__(self, other):       # для множення '*'
        mul_numer = self.numer * other.numer            # розрахунок нового чисельника
        mul_denom = self.denom * other.denom            # розрахунок нового знаменника
        # return Fraction(mul_numer, mul_denom)         # Повертає новий екземпляр типу даних (класу) 'Fraction' - без спрощення дробі
        return self.total_num_del(mul_numer, mul_denom) # Повертає новий екземпляр типу даних (класу) 'Fraction' через модуль 'total_num_del()'

    def __truediv__(self, other):       # для поділів '/'
        tr_numer = self.numer * other.denom           #
        tr_denom = self.denom * other.numer           #
        # return Fraction(tr_numer, tr_denom)         # Повертає новий екземпляр типу даних (класу) 'Fraction' - без спрощення дробі
        return self.total_num_del(tr_numer, tr_denom) # Повертає новий екземпляр типу даних (класу) 'Fraction' через модуль 'total_num_del()'


    def __add__(self, other):        # для додавання '+'
        add_numer = self.numer * other.denom + other.numer * self.denom  # Обчислює новий чисельник
        add_denom = self.denom * other.denom            # Обчислює новий знаменник
        # return Fraction(add_numer, add_denom)         # Повертає новий екземпляр типу даних (класу) 'Fraction' - без спрощення дробі
        return self.total_num_del(add_numer, add_denom) # Повертає новий екземпляр типу даних (класу) 'Fraction' через модуль 'total_num_del()'

    def __sub__(self, other):        # для віднімання '-'
        sub_numer = self.numer * other.denom - other.numer * self.denom  # Обчислює новий чисельник
        sub_denom = self.denom * other.denom            # Обчислює новий знаменник
        # return Fraction(sub_numer, sub_denom)         # Повертає новий екземпляр типу даних (класу) 'Fraction' - без спрощення дробі
        return self.total_num_del(sub_numer, sub_denom) # Повертає новий екземпляр типу даних (класу) 'Fraction' через модуль 'total_num_del()'

    def __eq__(self, other):        # для порівняння '=='
        return self.numer / self.denom == other.numer / other.denom

    def __gt__(self, other):        # для оператора більш `>`
        return self.numer / self.denom > other.numer / other.denom

    def __lt__(self, other):        # для оператора меньш `<`
        return self.numer / self.denom < other.numer / other.denom

    def total_num_del(self, new_numer, new_denom):      # Метод для вирахування спільного дільника двох чисел (ціле число) - для спрощення дробу
        max_del = math.gcd(new_numer, new_denom)        # повертає найбільший спільний дільник
        new_numer = int(new_numer / max_del)            # Ділимо чисельник на 'max_del'
        new_denom = int(new_denom / max_del)            # Ділимо знаменник на 'max_del'
        # new_numer //= max_del                         # цілочислений поділ з присвоєнням
        # new_denom //= max_del                         #
        return Fraction(new_numer, new_denom)           # Повертає новий екземпляр типу даних (класу) 'Fraction'

    def __str__(self):
        print(f"Fraction: {self.numer} / {self.denom}")
        return f"Fraction: {self.numer}, {self.denom}"



f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
# assert str(f_c) == 'Fraction: 21, 18'     # без спрощення дробі
assert str(f_c) == 'Fraction: 7, 6'         # зі спрощенням дробі

f_d = f_b * f_a
# assert str(f_d) == 'Fraction: 6, 18'      #
assert str(f_d) == 'Fraction: 1, 3'         #

f_e = f_a - f_b
# assert str(f_e) == 'Fraction: 3, 18'      #
assert str(f_e) == 'Fraction: 1, 6'         #

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
