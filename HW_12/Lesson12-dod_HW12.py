# 1.
# написати скрипт для видалення всіх файлів вказаної директорії
#
# 2.
# создать телефонную книгу с сохранением в файл txt
# добавление
# изменение контакта
# удаление
# поиск по имени



# 1. v1.
# **********************
# Видалення файлів у Python за допомогою модулів os, glob, shutil

import os
# from os import path
path_dir = "C:\\Temp_test"                  # КАТОЛОГ для тестування
if os.path.exists(path_dir):                # перевірка наявнсті каталога для тестування ("C:\Temp_test")
    print(f"Каталог {path_dir} в наявності !")
else:
    os.mkdir(path_dir)                      # створюємо каталог для тестування якщо нема ("C:\Temp_test")
    print(f"Каталога {path_dir} створений !")

# створюємо (з перевіркою) підкаталог 'Dir1'
file1_dir1, file2_dir1 = "hello1_dir1.txt", "hello2_dir1.txt"
# file2_dir1 = "hello2_dir1.txt"
path_dir1 = path_dir + "\\Dir1"
if not os.path.exists(path_dir1):
    os.mkdir(path_dir1)
#
# створюємо файли в підкаталогу 'Dir1'
# with open(path_dir1+"\\""hello1_dir1.txt", "w") as file1_dir1:	# вказуємо ім'я файлів
#     file1_dir1.write("wwwwww")
# with open(path_dir1+"\\""hello2_dir1.txt", "w") as file2_dir1:	#
#     file2_dir1.write("wwwwww")
# !!!!!
with open(path_dir1+"\\"+file1_dir1, "w") as f1_d1:	                # ім'я файлів через змінну
    f1_d1.write("wwwwww")
with open(path_dir1+"\\"+file2_dir1, "w") as f2_d1:	                #
    f2_d1.write("wwwwww")


# створюємо (з перевіркою) підкаталог 'Dir2'
file1_dir2, file2_dir2 = "hello1_dir2.txt", "hello2_dir2.txt"
# file2_dir2 = "hello2_dir2.txt"
path_dir2 = path_dir + "\\Dir2"
if not os.path.exists(path_dir2):
    os.mkdir(path_dir2)
#
# створюємо файли в підкаталогу 'Dir2'
with open(path_dir2+"\\"+file1_dir2, "w") as f1_d2:	#
    f1_d2.write("qqqqqqq")
with open(path_dir2+"\\"+file2_dir2, "w") as f2_d2:	#
    f2_d2.write("qqqqqqq")

# деякі операції з каталогами :
# os.chdir(path_dir)              # зміна поточного каталогу
# print(os.getcwd())              # вивід поточного каталогу
# lst = os.listdir(path_dir)      # повертає список підкаталогів та файлів за вказаним шляхом
# print(lst)

### видалення ФАЙЛІВ
## вказуя файли для видалення :
# os.remove(path_dir1+"\\"+file1_dir1)
# os.remove(path_dir1+"\\"+file2_dir1)

## за допомогою списку з вмісту (файлів) каталога :
# lst_file = os.listdir(path_dir1)
# print(lst_file)
# for file in lst_file: os.remove(path_dir1+"\\"+file)

## видалення по маскі файлів (з використання модуля 'glob')
# import glob
# for file in glob.glob(path_dir1+"/*.txt"): os.remove(file)      # видалення файлів по маски
# !!!!!
# from glob import glob                                           # АБО так :
# for file in glob(path_dir1+"/*"): os.remove(file)               # видалення всіх файлів
# for file in glob(path_dir2+"/*"): os.remove(file)               # видалення всіх файлів

### видалення КАТАЛОГІВ
##  видалення порожніх каталогів :
# os.rmdir(path_dir1)               # Видаляє  порожній каталог
# os.rmdir(path_dir2)

##  видалення каталогів з вмістом
import shutil
# shutil.rmtree(path_dir1)          # Видаляє каталог і весь його вміст
# shutil.rmtree(path_dir2)
# !!!!!
## за допомогою списку з вмісту (підкаталогів) каталога :
lst_dir = os.listdir(path_dir)
print(lst_dir)
# import shutil
# for dir in lst_dir: shutil.rmtree(path_dir+"\\"+dir)
from shutil import rmtree                       # АБО так :
for dir in lst_dir: rmtree(path_dir+"\\"+dir)

# 1. v2.
# **********************
# Видалення файлів у Python за допомогою модуля os
# import os
# path_dir = "C:\\Temp"
# try:
#     os.mkdir(path_dir)                      # створюємо каталог "C:\Temp"
# except:
#     print(f"Каталог {path_dir} вже створений")



# ==============================================
# # Specify the file to be deleted
# file_path = 'path/to/your/file.txt'
#
# try:
#     os.remove(file_path)
#     print(f"{file_path} has been deleted successfully")
# except FileNotFoundError:
#     print(f"{file_path} does not exist")
# except PermissionError:
#     print(f"Permission denied to delete {file_path}")
# except Exception as e:
#     print(f"Error occurred: {e}")
#
# # ## Видалення декілька файлів :
# #
# # for file in file_list: os.remove(file)
# #
#
#
# # ## Видалення файлів за допомогою символів підстановки :
# # import glob
# # for file in glob.glob('*.txt'): os.remove(file).
#
# # ***************
#
# # Видалення каталогів у Python за допомогою модуля os
# #
# import os
#
# # Specify the directory to be deleted
# dir_path = 'path/to/your/directory'
#
# try:
#     os.rmdir(dir_path)
#     print(f"{dir_path} has been deleted successfully")
# except FileNotFoundError:
#     print(f"{dir_path} does not exist")
# except OSError:
#     print(f"{dir_path} is not empty or cannot be deleted")
# except Exception as e:
#     print(f"Error occurred: {e}")
#
#
# # Використання модуля shutil для видалення каталогів
# import shutil
#
# # Specify the directory to be deleted
# dir_path = 'path/to/your/directory'
#
# try:
#     shutil.rmtree(dir_path)
#     print(f"{dir_path} and all its contents have been deleted")
# except FileNotFoundError:
#     print(f"{dir_path} does not exist")
# except PermissionError:
#     print(f"Permission denied to delete {dir_path}")
# except Exception as e:
#     print(f"Error occurred: {e}")
