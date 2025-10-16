def file_numbers():
    try:
        with open('Sadock.txt', 'r', encoding='utf-8') as file:
            numbers = [] # Создаю пустой массив
            for line in file:
                line = line.strip() # Убираю лишние пробелы и символы
                if line: # Если строка не пустая
                    try:
                        number = float(line) # Пытаюсь преобразовать строку в число
                        numbers.append(number) # Добавляю все вещественные числа из файла в пустой массив
                    except ValueError:
                        print(f"Пропущена некорректная строка: '{line}'")
                        continue # Переход к следующей строке файла при некорректной текущей строке

        if not numbers:
            print("В файле нет корректных числовых данных!")
            return # Выход из функции при отсутствии корректных числовых данных

        summa = sum(numbers) # Вычисляю сумму
        maximum = max(numbers) # Вычисляю максимум

        with open('Sadock.txt', 'a', encoding='utf-8') as file:
            file.write(f"Результаты обработки:\n")
            file.write(f"{summa}\n")
            file.write(f"{maximum}\n")

        print("Результаты успешно дописаны в файл 'numbers.txt'")
        print(f"Сумма чисел: {summa}")
        print(f"Максимальное число: {maximum}")

    except FileNotFoundError:
        print("Ошибка: файл 'Sadock.txt' не найден!")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

file_numbers() # Вызываю функцию