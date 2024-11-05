# В файле users.json хранится список пользователей с полями:
# имя, возраст, город и профессия. Напишите программу,
# которая считывает файл и выводит только тех пользователей,
# которые старше 30 лет и работают в указанной профессии.
import json

list1 = []
with (open("users.json", "r", encoding="utf-8") as file):
    data: dict = json.load(file)
    for d in range(len(data)):
        if data[d]["age"] > 30 and data[d]["profession"] == "программист":
            list1.append(data[d])
print(list1)