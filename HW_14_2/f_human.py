# Модуль 'f_human.py'

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
