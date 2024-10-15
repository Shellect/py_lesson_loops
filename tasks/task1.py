"""
Задание 1
Пользователь вводит с клавиатуры два числа. Нужно
посчитать сумму чисел в указанном диапазоне, а также
среднеарифметическое.
"""
from tasks.functions import user_input
def task1():
    print("Программа для подсчёта суммы чисел")

    print("Введите нижнюю границу диапазона")
    a = user_input()

    print("Введите верхнюю границу диапазона")
    b = user_input()

    accumulator = 0
    r = range(a, b)
    for i in r:
        accumulator = accumulator + i

    print(f"Сумма чисел в диапазоне: {accumulator}")
    print("Среднее арифметическое всех чисел: {}".format(accumulator / len(r)))
