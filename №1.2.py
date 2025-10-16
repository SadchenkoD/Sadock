try:
    with open('Sadock.txt', 'r', encoding='utf-8') as file:
        numbers = [] # Создаю пустой массив
        for line in file:
            line = line.strip()  # Чищу строку от лишних символов и пробелов
            if line:  # Если строка не пустая
                numbers.append(float(line)) # Добавляю все вещественные числа из файла в пустой массив

    summa = sum(numbers) # Вычисляю сумму
    maximum = max(numbers) # Вычисляю максимум

    with open('Sadock.txt', 'a', encoding='utf-8') as file:
        file.write(f"{summa}\n") # Дописываю сумму чисел в файл
        file.write(f"{maximum}\n") # Дописываю максимальное число в файл

    print("Результаты успешно дописаны в файл 'numbers.txt'")
    print(f"Сумма чисел: {summa}")
    print(f"Максимальное число: {maximum}")

except FileNotFoundError:
    print("Ошибка: файл 'Sadock.txt' не найден!")
except ValueError as e:
    print(f"Ошибка: в файле содержатся некорректные данные - {e}")
except Exception as e:
    print(f"Произошла неизвестная ошибка: {e}")