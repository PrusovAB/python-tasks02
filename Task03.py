# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# *Пример:*

# - Для n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Сумма чисел = 14.0717

def arrayRezult():
    try:
        array = []
        number = int(input("Введите  число : "))
        for n in range(1, number+1):
            sum = (1 + 1/n)**n
            array.append(round(sum, 4))
        if number < 0:
            print("Вы ввели отрицательное число. Введите положительное целое! ")
            arrayRezult()
    except ValueError:
        print("Вы ввели не то введите целое число")
        arrayRezult()
    return array


a = arrayRezult()
print(*a)


def sumArray(array):
    sum = 0
    for i in array:
        sum += i
    return sum


print(f"Сумма чисел = {sumArray(a)}")
