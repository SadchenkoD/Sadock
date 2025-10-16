def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.

    Параметры:
        - text (str): строка;
        - shift (int): сдвиг.

    Результат:
        str: измененная строка.

    Исключения:
        - ValueError: некорректные параметры
    """
    lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = []  # Добавляю пустой список

    # Проверяем, что shift является целым числом
    if not isinstance(shift, int):
        raise ValueError("Сдвиг должен быть целым числом")

    for char in text:
        if char in lower:
            index = lower.index(char)  # Номер буквы в алфавите
            new_index = (index + shift) % len(lower)  # Обеспечиваю циклический сдвиг (после "я" идет "а")
            result.append(lower[new_index])  # Добавляю букву в список
        elif char in upper:
            index = upper.index(char)  # Номер буквы в алфавите
            new_index = (index + shift) % len(upper)  # Обеспечиваю циклический сдвиг (после "я" идет "а")
            result.append(upper[new_index])  # Добавляю букву в список
        else:
            result.append(char)

    return ''.join(result)  # Объединяю все символы из списка в одну строку и возвращаю её


# Основная программа с обработкой исключений
try:
    text = input("Введите предложение: ")

    # Проверяю, что введен текст
    if not text.strip():
        raise ValueError("Предложение не может быть пустым")

    shift_input = input("Введите сдвиг: ")
    shift = int(shift_input)  # Может вызвать ValueError

    # Проверяю разумность сдвига (опционально)
    if abs(shift) > 100:
        print("Очень большой сдвиг может ухудшить читаемость")

    felix = ceasar(text, shift)  # Зашифровка
    pazik = ceasar(felix, -shift)  # Расшифровка

    print("Зашифрованная строка:", felix)
    print("Расшифрованная строка:", pazik)

except ValueError as err:
    if "invalid literal" in str(err):
        print("Ошибка: Сдвиг должен быть целым числом")
    else:
        print(f"Ошибка ввода: {err}")
except KeyboardInterrupt:
    print("\nПрограмма прервана пользователем")
except Exception as err:
    print(f"Неизвестная ошибка: {err}")
finally:
    print("Работа программы завершена")