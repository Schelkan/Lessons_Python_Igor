# На вхід функції correct_sentence передається два речення. Необхідно повернути їх виправлену копію так, щоб вони завжди починалися з великої літери та закінчувалися крапкою.
# Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою, додавати ще одну не потрібно, це буде помилкою
# Вхідні аргументи: string. Вихідні аргументи: string.

#  данні для перевірки роботи програми
# my_text = "greeting, friends"         # ->  "Greetings, friends."
# my_text = "hello"                     # ->  "Hello."
# my_text = "Greetings. Friends"        # ->  "Greetings. Friends."
my_text = "Greetings, friends."       # ->  "Greetings, friends."
# my_text = "greetings, friends."       # ->  "Greetings, friends."

def correct_sentence(text):
    text = text.rstrip(".")         # забирає справа символ '.'
    text = text.title()             # кожне слово з великої літери
    print(f"{text}.")
    # return f"{text}."
correct_sentence(my_text)

# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')


