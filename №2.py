def power(x, y=2):
    """Вернуть x^y.

    Параметры:
        - x (int или float): основание;
        - y (int): показатель степени.

    Результат:
        - int или float.

    Исключения:
        - ValueError: некорректные значения параметров.
        - RecursionError: слишком большая глубина рекурсии.
    """
    if y < 0:
        raise ValueError("Показатель степени не может быть отрицательным")
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

# Основная программа с обработкой исключений
try:
    x = int(input("x="))
    y = int(input("y="))
    result = power(x, y)
    print(f"{x}^{y} = {result}")
except ValueError as err:
    if "invalid literal" in str(err):
        print("Ошибка: Введите целые числа для x и y")
    else:
        print("Ошибка:", err)
except RecursionError:
    print("Ошибка: Слишком большая степень. Используйте меньшие значения для y")
except Exception as err:
    print("Неизвестная ошибка:", err)