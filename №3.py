def Sadock(data):
    result_set = set(data) # Преобразование списка в множество

    print(f"Множество: {result_set}")
    print(f"Мощность множества (количество элементов): {len(result_set)}")

    return result_set
spisok= [17, 7, -100, 0.9, 69, 5, 52, 19, 22]
Sadock(spisok)