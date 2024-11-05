#   В файле employees.csv содержится список сотрудников
# с полями: имя, возраст, должность, зарплата.
# Напишите программу, которая считывает данные
# и выводит только тех сотрудников,
# у которых зарплата больше 50,000.
import csv

with open("employees.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    emp = []
    for i in reader:
        if int(i["salary"]) > 50000:
            emp.append(i["name"])
    print(emp)