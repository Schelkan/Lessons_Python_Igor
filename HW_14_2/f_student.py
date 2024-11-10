# Модуль 'f_student.py'

from f_human import Human           # з модуля (файлу) 'f_human.py' імпортуємо клас 'Human'
class Student(Human):               # успадковуємося від класу Human

    def __init__(self, gender, age, first_name, last_name, record_book):        # конструктор класу (ініціалізатор класу)
        super().__init__(gender, age, first_name, last_name)    # посилання на базовий клас, отримуємо доступ до елементів базового класу
        self.record_book = record_book                          # змінна класу (параметри)

    def __str__(self):
        # print(f"Human name : {self.first_name} {self.last_name}. Gender : {self.gender}. Age : {self.age}. Record book : {self.record_book}")
        return (f"{super().__str__()}. Record book : {self.record_book}")

    def __eq__(self, compar_student):           # метод порівняння на рівність ('compar_student' - об'єкт, 'Student' - клас)
        if isinstance(compar_student, Student):
            # return True
            return str(self) == str(compar_student)
        return False

    def __hash__(self):                         # метод розрахунку хеш для незмінних об'єктів (для порівняння)
        return hash(str(self))