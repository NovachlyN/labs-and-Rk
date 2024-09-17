# Лабораторная работа 1.
# Базовый калькулятор

# Получение операции от пользователя
operation = input("Введите операцию: ")
try:

# Получение двух чисел от пользователя
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
except ValueError:
        print("Ошибка:введены некорректные числа")
        exit()
def calculate(operation,num1,num2):
# Выполнение операции
    if operation == "+":
        result = num1 + num2
        print(f"Результат сложения: {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Результат вычитания: {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Результат умножения: {result}")
    elif operation == "/":
        result = num1 / num2
        print(f"Результат деления: {result}")
    else:
        print("Операция не поддерживается")
result=calculate(operation,num1,num2)