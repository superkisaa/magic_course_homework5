# Напишите программу, которая считывает данные из
# CSV-файла sales.csv, где содержатся данные о продажах
# (например, дата, товар, количество, цена).
# Программа должна вывести:
# - Общую сумму продаж.
# - Товар с наибольшим числом продаж.
import csv

with open("sales.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    sum = 0
    dict1 = {}
    for i in reader:
        print(i)
        sum += float(i["price"])*float(i["quantity"])
        if i["product"] in dict1:
            dict1[i["product"]] += float(i["quantity"])
        else:
            dict1[i["product"]] = float(i["quantity"])
    max = 0
    max_key = 0
    for j in dict1:
        if dict1[j] > max:
            max = dict1[j]
            max_key = j
    print(f'Общая сумма продаж: {sum}')
    print(f'Товар с наибольшим числом продаж: {max_key}')
