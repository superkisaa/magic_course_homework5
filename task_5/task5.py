# Система учета заказов

# У вас есть JSON-файл orders.json,
# содержащий данные о заказах интернет-магазина.
# Каждый заказ включает информацию о клиенте,
# заказанных товарах, количестве и цене.

# Напишите программу, которая:
# Выводит общую сумму каждого заказа.
# Находит клиента с наибольшей суммой заказа и выводит его имя и сумму.
import json

with open("orders.json", "r", encoding="utf-8") as file:
    data = json.load(file)
max = 0
for order in data["orders"]:
    sum = 0
    for item in order["items"]:
        sum += item["price"]*item["quantity"]
        if sum > max:
            max = sum
    print(f'Общая сумма заказа: {sum}')
print(f'Максимальная сумма заказа: {max}')


