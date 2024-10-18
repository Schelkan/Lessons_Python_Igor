# Функція second_index приймає як параметри 2 рядки. Вам необхідно знайти індекс другого входження
# шуканого рядка у рядку для пошуку.
# Розберемо перший приклад, де необхідно знайти друге входження "s" в слові "sims".
# Якби нам треба було знайти її перше входження, то тут все просто: за допомогою функції
# index або find ми можемо дізнатися, що "s" - це перший символ у слові "sims",
# а значить індекс першого входження дорівнює 0. Але нам Необхідно визначити другу "s",
# а вона четверта за рахунком. Значить індекс другого входження (і у відповідь питання) дорівнює 3.
# Рядок, який потрібно знайти, може складатися з кількох символів.
# Input: Два рядки (String).  Output: Int or None

# my_text, my_symbol = "find the river", "e"        # параметри для функції 'second_index()'
# my_text, my_symbol = "Hello, hello", "lo"
my_text, my_symbol = "Hello, hello", "ello"
# my_text, my_symbol = "hi", "h"

def second_index(text, some_str):
    ind_symbol1 = text.find(some_str)               # перше входження шуканого рядку
    # len_some_str = len(some_str)                  # довжина шуканого рядку
    ind_symbol2 = text.find(some_str, ind_symbol1 + len(some_str) + 1)  # друге входження шуканого рядку
    if ind_symbol2 == -1:
        print("індекс другого входження шуканого рядка у рядку для пошуку не знайдений")
        return None
    else:
        print(ind_symbol2)              # для контролю
        return ind_symbol2

second_index(my_text, my_symbol)

# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')