def dan_sigma(strings): # Создаю функцию
    max_len = max(len(s) for s in strings) # Вычисляю максимальную длину строки
    return [s.ljust(max_len, '_') for s in strings] # Возвращаю список преобразованных строк одинаковой длины

strings = ["Брат", "Сестра", "Мама" , "Папа", "Дядя", "Тетя", "Крестный", "Крестная", "Дедушка", "Бабушка", ]
result = dan_sigma(strings)
print("Вывод нового списка из строк одинаковой длины:")
print(result)
