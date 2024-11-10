# У цьому завданні Вам необхідно зробити дві речі на підставі попереднього ДЗ.
#
# 1. До класу Студента необхідно додати метод порівняння. Порівнювати можна за тими рядками, які повертає метод str
# Для того, щоб спрацювала коректно ось ця перевірка:
# assert gr.find_student('Jobs') == st1
# 2. Рознесіть класи, які використовували під час виконання завдання про групу студентів за модулями.
# Переконайтеся у працездатності проекту – створіть окремо файл main.py,
# у якому необхідно імпортувати потрібні класи та запустити код перевірки.
# 3. Якщо при спробі додавання студента до групи ви побачите помилку:
# self.group.add(student)
# TypeError: unhashable type: 'Student'
# то додайте до класу студента метод hash :  def __hash__(self): return hash(str(self))


from f_student import Student
from f_group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 30, 'Mike', 'Table', 'AN142')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st3)     # для перевірки
print(gr)

assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
# print("OK")

# gr.delete_student('Taylor')
# print(gr) # Only one student
