# Завдання 1
# 2.	Запитайте користувача про його ім'я та виведіть привітання з використанням введеної назви.

def user_congratulation():
    name = input("Вкажіть ваше ім'я \n")
    print(f"Вітаю, {name}")
user_congratulation()

# Завдання 2
# 4.	Напишіть функцію, яка приймає рядок та повертає його обернений варіант. Наприклад, "hello" повинно повернути "olleh".
def reverse_user_input(string):
    return string[::-1]

user_input = input("Enter the string \n")
print(reverse_user_input(user_input))

# Завдання 3
# 2.	Створіть функцію, яка приймає список чисел та повертає новий список, який містить лише парні числа.

def even_nums(list):
    return [num for num in list if num % 2 == 0]

array =[]
while True:
    try:
        num = int(input("Введіть число (для виходу введіть -1) \n"))
        if num == -1:
            break
    except ValueError:
        print("Ви ввели не число. Переходимо до наступногоч числа")
        continue
    array.append(num)
print(even_nums(array))

# Завдання 4
# 2.	Реалізуйте програму для роботи з API. Використовуйте бібліотеку requests, щоб отримати дані з публічного API та вивести їх на екран.

import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()   
    print("Факт про кітиків:", data['fact'])

else:
    print("Помилка. Код:", response.status_code)