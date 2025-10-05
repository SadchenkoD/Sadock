def sort_corteg(t): # Объявляю функцию
    if all(isinstance(x, int) for x in t): # Проверяю, все ли элементы целые числа
        return tuple(sorted(t)) # Если все целые - сортируем кортеж по возрастанию
    else:
        return t # Если есть нецелые - возвращаем исходный

corteg1 = (-10, 5, 17, 0.5, 99)

print(f"Результат: {sort_corteg(corteg1)}")
print()