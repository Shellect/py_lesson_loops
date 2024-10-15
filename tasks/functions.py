def user_input():
    while True:
        try:
            return int(input(">>> "))
        except ValueError:
            print("Неверный ввод!")