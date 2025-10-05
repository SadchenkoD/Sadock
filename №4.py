from collections.abc import Hashable
def Sadochek(spisok):

    result_set = set() # создаем пустое множество

    for item in spisok:
        if isinstance(item, Hashable): # проверка на хешируемость
            result_set.add(item) # добавление элемента в пустое множество

    return result_set
spisok = [1, "hello", [1, 2], ("tuple",), {"key": "value"}]

print("Получившееся множество:")
print(Sadochek(spisok))
