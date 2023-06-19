import os

curremt_path = os.path.abspath(__file__) # дает абсолютный путь до файла
print(curremt_path)

parent_path = os.path.join(curremt_path, '..') # join - позволяет достраивать путь
print(parent_path)

def recurs(count):
    print(count)
    if count == 5:
        return
    recurs(count+1)
    print(count)
recurs(0)

def power(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a*power(a,b-1)
print(power(2,3))

def fact(a):
    if a == 1:
        return 1
    else:
        return a*fact(a-1)
print(fact(5))

def get_all_files(path):
    for name in os.listdir(path): # возвращает список названи1 всех файлов (папок)
        new_path = os.path.join(path, name)
        if os.path.isdir(new_path): # проверяет является ли папкой
            print('Папка', name)
            get_all_files(new_path)
        else:
            print('  ---', name)

get_all_files('C:\Xiaomi')
