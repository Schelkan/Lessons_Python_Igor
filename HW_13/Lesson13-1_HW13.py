# Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# На його основі створіть клас Студент (перевизначте метод виведення інформації).
# Створіть клас Група, екземпляр якого складається з об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.
# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.


class Human:                         # базовий клас

    def __init__(self, gender, age, first_name, last_name):     # конструктор класу (з параметрами) - створює екземпляр об'єкту
        self.gender = gender         # змінни класу (параметри)
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):              # метод, що виводить інформацію про людину
        print(f"Human name : {self.first_name} {self.last_name}. Gender : {self.gender}. Age : {self.age}.")
        return (f"Human name : {self.first_name} {self.last_name}. Gender : {self.gender}. Age : {self.age}.")

class Student(Human):               # успадковуємося від класу Human

    def __init__(self, gender, age, first_name, last_name, record_book):        # конструктор класу (ініціалізатор класу)
        super().__init__(gender, age, first_name, last_name)    # посилання на базовий клас, отримуємо доступ до елементів базового класу
        self.record_book = record_book                          # змінна класу (параметри)

    def __str__(self):
        print(f"Human name : {self.first_name} {self.last_name}. Gender : {self.gender}. Age : {self.age}. Record book : {self.record_book}")
        return (f"{super().__str__()}. Record book : {self.record_book}")


class Group:

    def __init__(self, number_gr):          # конструктор класу
        self.number_gr = number_gr          # змінни класа
        self.group = set()                  # створюємо пустий список групи студентів

    def add_student(self, student):         # метод класу - додавання студента в групу
        self.group.add(student)             # додаємо студента в список групи
        # print(f'Студента : {student.last_name} в групу {self.number_gr} додано')

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
            all_students = all_students + student.last_name +"\n"
        # print(f"Студенти групи {self.number_gr} : \n{all_students}")
        return f'Number : {self.number_gr}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')  #Створює екземпляр студента
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# #
gr = Group('PD1')                   # Створює екземпляр групи
# print(gr)
gr.add_student(st1)                 # Додає студента до групи
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Jobs')
gr.delete_student('Taylor')
print(gr)  # Only one student
#
gr.delete_student('Taylor')  # No error!