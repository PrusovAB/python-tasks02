# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def arrayMultip():
    try:
        array = []
        sum = 1
        number = int(input("Введите целое число от 1 до N: "))
        for i in range(1, number+1):
            sum *= i
            array.append(sum)
        if number < 0:
            print("Вы ввели отрицательное число. Введите положительное целое! ")
            arrayMultip()
    except ValueError:
        print("Вы ввели не то введите целое число")
        arrayMultip()
    return array


print(*arrayMultip())
