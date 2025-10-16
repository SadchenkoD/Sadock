print("Введите последовательность целых чисел")
print("Для завершения ввода введите 0")
summa = 0 # Сумма чисел
kachalka = 0 # К-во чисел

while True: # Бесконечный цикл
    number = int(input("Введите число: "))
    if number == 0:
        break

    summa += number
    kachalka += 1

print(f"Сумма чисел: {summa}")
print(f"Количество чисел: {kachalka}")