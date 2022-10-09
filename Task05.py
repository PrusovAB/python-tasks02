def createList():
    try:
        array = []
        number = int(input("Введите  размерность списка N: "))
        if number < 0:
            print("Введите целое положительное число!!!!")
            createList()
        for n in range(number+1):
            array.append(n)

    except ValueError:
        print("Вы ввели не то введите целое число")
        createList()
    return array


a = createList()
print(f"Наш созданый массив = {a}")


def mixArray(array):
    newArray = []

    for i in array:
        if i % 2 == 0:
            newArray.append(array[i])

    for j in array:
        if j % 2 != 0:
            newArray.append(array[j])
    b = newArray[::-1]

    return b


b = print(f"Перемешанный список = {mixArray(a)}")
