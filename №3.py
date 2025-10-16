def Toni_Rayt(n):
    """Найти наиболее часто встречаемое отчество.

    Параметры:
        - n (int): количество человек

    Исключения:
        - ValueError: некорректный ввод данных
        - IndexError: отсутствие отчества в ФИО
    """
    count = {}  # Создаю пустой словарь

    for i in range(n):
        try:
            fio = input(f"Введите ФИО человека {i + 1}: ").split()

            # Проверяю, что введено достаточно частей ФИО
            if len(fio) < 3:
                raise ValueError(f"Ожидается Фамилия Имя Отчество, получено: {' '.join(fio)}")

            otche_nash = fio[2]  # Нахожу отчество
            count[otche_nash] = count.get(otche_nash, 0) + 1  # Получаю значение из словаря и увеличиваю счетчик на 1

        except ValueError as err:
            print(f"Ошибка ввода у человека {i + 1}: {err}")
        except Exception as err:
            print(f"Неизвестная ошибка у человека {i + 1}: {err}")

    return count


# Основная программа с обработкой исключений
try:
    n = int(input("Введите кол-во человек: "))

    # Проверяю корректность количества людей
    if n <= 0:
        raise ValueError("Количество человек должно быть положительным числом")

    count = Toni_Rayt(n)

    # Проверяю, есть ли данные для анализа
    if not count:
        print("Нет данных для анализа. Все введенные ФИО содержали ошибки.")
    else:
        most_common = max(count, key=count.get)  # Наиболее частое отчество
        print(f"Самое популярное отчество: '{most_common}'")
        print(f"Количество людей с этим отчеством: {count[most_common]}")
        print(f"Всего обработано ФИО с отчествами: {sum(count.values())} из {n}")

except ValueError as err:
    if "invalid literal" in str(err):
        print("Ошибка: Введите целое число для количества человек")
    else:
        print(f"Ошибка ввода: {err}")
except KeyboardInterrupt:
    print("\nПрограмма прервана пользователем")
except Exception as err:
    print(f"Неизвестная ошибка: {err}")