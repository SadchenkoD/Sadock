# Задание 2.1
print("Введите последовательность целых чисел:")

summa = 0
gym = 0
number = int(input("Введите число: "))

while number != 0:
    summa += number
    gym += 1
    number = int(input("Введите число: "))

print(f"Сумма чисел: {summa}")
print(f"Количество чисел: {gym}")

# Задание 2.2
n = int(input("Введите число n: "))

print(f"Числа из последовательности не превышающие {n}:")
for i in range(0, n + 1, 5):
    print(i) 