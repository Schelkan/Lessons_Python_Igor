# Створити клас цифрового лічильника. У класі реалізувати методи:
#
# встановлення максимального значення лічильника,
# встановлення мінімального значення лічильника
# встановлення початкового значення лічильника
# метод step_up збільшує лічильник на 1. Метод можна викликати до тих пір, поки значення досягне максимуму.
# При досягненні максимуму слід викинути (raise) виняток ValueError, з описом, що досягнуто максимумуʼ
# метод step_down зменшує лічильник на 1. Метод можна викликати до тих пір, поки значення не досягне мінімуму.
# При досягненні мінімуму потрібно викинути (raise) виняток ValueError, з описом, що досягнутий мінімум
# повернення поточного значення лічильника
# Початкове, мінімальне та максимальне значення лічильника також можуть бути додані в метод ініціалізації екземпляра класу.
#
# Приблизний каркас для класу та варіанти перевірки. Вам потрібно дописати необхідне замість pass


class Counter:                  # Клас лічильник

   def __init__(self, current=1, min_value=0, max_value=10):        # конструктор класу
       self.current = current                       # встановлення початкового значення лічильника
       self.min_value = min_value                   # встановлення мінімального значення лічильника
       self.max_value = max_value                   # встановлення максимального значення лічильника


   def set_current(self, start):        # встановлення початкового значення лічильника
       if self.min_value <= start <= self.max_value:
           self.current = start
       else:                            # обробка винятку 'ValueError'
           raise ValueError("Початкове значення повинно бути в межах 'self.min_value' та 'self.max_value'")

   def set_max(self, max_max):          # встановлення максимального значення лічильника
       self.max_value = max_max
       if self.max_value < self.current or self.max_value < self.min_value:
           raise ValueError("Нове максимальне значення повинно бути більш початкового та мінімального значення.")

   def set_min(self, min_min):          # встановлення мінімального значення лічильника
       self.min_value = min_min
       if self.min_value > self.current or self.min_value > self.max_value:
           raise ValueError("Нове мінімальне значення повинно бути меньш початкового та максимального значення.")

   def step_up(self):                   # метод step_up збільшує лічильник на 1
       if self.current < self.max_value:
           self.current += 1
       else:                            # обробка винятку 'ValueError'
           raise ValueError("Значення лічильника досягнуло максимуму")

   def step_down(self):                 # метод step_down зменшує лічильник на 1
       if self.current > self.min_value:
           self.current -= 1
       else:                            # обробка винятку 'ValueError'
           raise ValueError("Значення лічильника досягнуло мінімуму")

   def get_current(self):               # повернення поточного значення лічильника
       return self.current

counter = Counter()
counter.set_current(7)
# print(counter.current)      # для перевірки
counter.step_up()
counter.step_up()
counter.step_up()
#counter.step_up()            # для перевірки
# print(counter.current)
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'


