import os
import time

print('Текущая директория:', os.getcwd())
directory = os.getcwd()
for i in os.walk('..'):
    print(i)
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print('Папки: ', dirs)
print('Файлы: ', file)
print('Полный путь к файлу: ', os.path.join(directory))
print('Время последнего изменения файла:', os.path.getmtime(directory))
print('Размер файла: ', os.path.getsize(directory))
print('Родительская директория файла: ', os.path.dirname(directory))