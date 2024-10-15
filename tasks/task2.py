"""
Пользователь вводит с клавиатуры число. Требуется
посчитать факториал числа. Например, если введено 3,
факториал числа 1*2*3 = 6.
Формула для расчета факториала: n! = 1*2*3…*n, где
n — число для расчета факториала.
"""
from tasks.functions import user_input
def task2():
    print("Программа подсчёта факториала")
    print("Введите любое целое положительное число")
    while True:
        n = user_input()
        if n < 0 or isinstance(n, float):
            print("Для отрицательных и дробных чисел нельзя вычислить факториал!")
            continue
        break

    result = 1
    counter = 1
    while n >= counter:
        result = result * counter
        counter = counter + 1

    print(f"Факториал {n} равен {result}")