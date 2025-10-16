# Задание 3.1
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
minimum = min(a, b) # Нахожу минимальное
maximum = max(a, b) # Нахожу максимальное

print(f"\nЧисла в строчку:")
for i in range(minimum, maximum + 1):
    print(i, end=" ")

print(f"\nЧисла столбиком:")
for i in range(maximum, minimum - 1, -1):
    print(i)

# Задание 3.2
p = int(input("Введите грузоподъемность грузовика (кг): "))
n = int(input("Сколько предметов нужно загрузить? "))
total_mass = 0

print("Введите массу каждого предмета (кг):")
for i in range(n):
    massa = float(input(f"Масса предмета {i+1}: "))
    total_mass += massa

print(f"Общая масса груза: {total_mass} кг")
print(f"Грузоподъемность грузовика: {p} кг")

if total_mass <= p:
    print("Перевозка возможна")
else:
    print("Перевозка невозможна")
