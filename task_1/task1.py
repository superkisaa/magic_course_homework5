# Напишите программу, которая сравнивает два JSON-файла
# (file1.json и file2.json) и выводит различия между ними.
# Программа должна определить, какие ключи или значения отличаются.
# Сравнивать только ключи и значения первого уровня.
import json

with open("file1.json", "r", encoding="utf-8") as file1:
    data1: dict = json.load(file1)
with open("file2.json", "r", encoding="utf-8") as file2:
    data2: dict = json.load(file2)
print(data2.keys())

for k in data1.keys():
    if k in data2.keys():
        if data1[k] == data2[k]:
            continue
        else:
            print(f'Значения для ключа {k} отличаются. В первом файле {data1[k]}, а во втором {data2[k]}')
    else:
        print(f'Ключа {k} нет во втором файле')

for k in data2.keys():
    if k in data1.keys():
        continue
    else:
        print(f'Ключа {k} нет в первом файле')

