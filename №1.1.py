print("Ввести вещественные числа через пробел:")


numbers = input(" ") # Ввожу числа в одной строке
list = numbers.split() # Разделяем их

with open('Sadock.txt', 'w', encoding='utf-8') as file: # Открываю файл для записи
    for number in list:
        file.write(number + '\n') # Каждое число на отдельной строке

print("Числа успешно записаны в файл 'Sadock.txt'")

