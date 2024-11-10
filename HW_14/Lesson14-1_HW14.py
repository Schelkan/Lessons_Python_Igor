#  1.
# Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# На його основі створіть клас Студент (перевизначте метод виведення інформації).
# Створіть клас Група, екземпляр якого складається з об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.
# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.
#  2.
# Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів,
# було порушено виняток користувача.
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації. І обробити його поза межами класу.
# Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента

class GroupLimitException(Exception):            # обробка винятку
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name


class Human:                         # базовий клас

    def __init__(self, gender, age, first_name, last_name):     # конструктор класу (з параметрами) - створює екземпляр об'єкту
        self.gender = gender         # змінни класу (параметри)
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):              # метод, що виводить інформацію про людину
        # print(f"Human name : {self.first_name} {self.last_name}. Gender : {self.gender}. Age : {self.age}.")
        return (f"Human name : {self.first_name} {self.last_name}. Gender : {self.gender}. Age : {self.age}.")

    def show_info(self):
        print(self.__str__())

class Student(Human):               # успадковуємося від класу Human

    def __init__(self, gender, age, first_name, last_name, record_book):        # конструктор класу (ініціалізатор класу)
        super().__init__(gender, age, first_name, last_name)    # посилання на базовий клас, отримуємо доступ до елементів базового класу
        self.record_book = record_book                          # змінна класу (параметри)

    def __str__(self):
        # print(f"Human name : {self.first_name} {self.last_name}. Gender : {self.gender}. Age : {self.age}. Record book : {self.record_book}")
        return (f"{super().__str__()}. Record book : {self.record_book}")


class Group:

    def __init__(self, number_gr, student_limit = 10):          # конструктор класу
        self.number_gr = number_gr              # змінни класа
        self.group = set()                      # створюємо пустий список групи студентів
        self.student_limit = student_limit      # макс.кількість студентів у групі

    def add_student(self, student):             # метод класу - додавання студента в групу
        if len(self.group) < self.student_limit:
            self.group.add(student)             # додаємо студента в список групи
            print(f'Студента : {student.first_name} {student.last_name} в групу {self.number_gr} додано')
        else:
            raise GroupLimitException(f"Кількість студентів повинна бути не більш : {self.student_limit}", self.number_gr)
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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')  #Створює екземпляр студента
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Alex', 'Taylor', 'AN145')
st4 = Student('Female', 25, 'Bob', 'Taylor', 'AN145')
st5 = Student('Female', 25, 'Mike', 'Taylor', 'AN145')
st6 = Student('Female', 25, 'Mishel', 'Taylor', 'AN145')
st7 = Student('Female', 25, 'Olga', 'Taylor', 'AN145')
st8 = Student('Female', 25, 'Ivanko', 'Taylor', 'AN145')
st9 = Student('Female', 25, 'Oles', 'Taylor', 'AN145')
st10 = Student('Female', 25, 'Vova', 'Taylor', 'AN145')
st11= Student('Female', 25, 'Li', 'Taylor', 'AN145')
# #
gr = Group('PD1')                   # Створює екземпляр групи
# print(gr)
try:
    gr.add_student(st1)                 # Додає студента до групи
    gr.add_student(st2)
    gr.add_student(st3)                 # Додає студента до групи
    gr.add_student(st4)
    gr.add_student(st5)                 # Додає студента до групи
    gr.add_student(st6)
    gr.add_student(st7)                 # Додає студента до групи
    gr.add_student(st8)
    gr.add_student(st9)                 # Додає студента до групи
    gr.add_student(st10)
    gr.add_student(st11)                # Додає студента до групи
except GroupLimitException as error:
    print(error)
except Exception as error:
    print(error)

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Jobs')
# gr.delete_student('Taylor')
#
# gr.delete_student('Taylor')  # No error!


