# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


def sumNumber():
    try:
        sum = 0
        number = input(
            "Введите любое число и получите сумму его цифр: ").replace(".", "").replace("-", "")

        for i in number:
            sum += int(i)
    except ValueError:
        print("Вы ввели не число попробуйте еще раз")
        sumNumber()
    return sum


print(f"Сумма введенного числа = {sumNumber()}")
