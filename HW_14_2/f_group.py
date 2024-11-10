## Модуль 'f_group.py'

# from f_student import Student               # з модуля (файлу) 'f_student.py' імпортуємо клас 'Student'
class Group:

    def __init__(self, number_gr):
        self.number_gr = number_gr          # змінни класа
        self.group = set()                  # створюємо пустий список групи студентів

    def add_student(self, student):         # метод класу - додавання студента в групу
        self.group.add(student)             # додаємо студента в список групи

    def delete_student(self, last_name):    # метод класу - видалення студента з групи
        f_student = self.find_student(last_name)
        if f_student:
            self.group.remove(f_student)
            # print(f'Студента {f_student.last_name} з групи {self.number_gr} видалено')

    def find_student(self, last_name):      # метод класу - пошук студента в групі
        for student in self.group:
            if student.last_name == last_name:
                # print(f"Студент {last_name} знайдений")
                return student
            # else:
                # print(f"Студент {last_name} не знайдений")
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            # all_students = all_students + student.last_name +"\n"
            all_students += student.__str__() + "\n"
        # print(f"Студенти групи {self.number_gr} : \n{all_students}")
        return f'Number : {self.number_gr}\n{all_students}'
