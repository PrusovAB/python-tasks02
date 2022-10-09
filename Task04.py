def split(s):
    return [int(i) for i in s]


def readFile():
    file = open("text.txt", "rt", encoding="utf-8")
    array = file.read()
    b = split(array)
    file.close()
    return b


b = readFile()


def rezultArrayMulti(ar):
    try:
        array = []
        number = int(input("Введите  число N: "))
        multi = 1
        if number < 0:
            print("Введите целое положительное число!!!!")
            rezultArrayMulti(ar)
        for n in range(-number, number+1):
            array.append(n)
        print(f"Массив в фаиле = {ar}")
        print(f"Наш созданный массив от -N до N = {array}")
        for i in range(len(ar)):
            for j in range(len(array)):

                if ar[i] == j:
                    multi *= array[j]

    except ValueError:
        print("Вы ввели не то введите целое число")
        rezultArrayMulti(ar)
    return multi


print(f"Наш результат = {rezultArrayMulti(b)}")
