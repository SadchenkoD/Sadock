def felix_pazik(corteg, element):

    if element in corteg:
        first_index = corteg.index(element)  # индекс первого вхождения элемент
        if element in corteg[first_index + 1:]:
            second_index = corteg.index(element, first_index + 1) # Пытаемся найти индекс второго вхождения, начиная поиск после первого
            return corteg[first_index:second_index + 1]  # Возвращает срез от первого до второго вхождения включительно

        else:
            return corteg[
                   first_index:]  # возвращает срез от первого элемента до конца кортежа, если второго вхождения нет
    else:
        return ()  # возвращает пустой кортеж, если элемента нет в кортеже

old_corteg = (0, 5, 17, 4, 69, 52, 47, 16, 7.7, 17, -100, 27)
element = 17
new_corteg = felix_pazik(old_corteg, element)

print(f"Изначальный кортеж: {old_corteg}")
print(f"Элемент: {element}")
print(f"Новый кортеж: {new_corteg}")
