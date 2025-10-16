a = int(input("Введите начальное число a: "))
b = int(input("Введите конечное число b: "))
c = int(input("Введите число c: "))

print(f"Числа от {a} до {b}, кратные {c}:")
for number in range(a, b + 1):
    if number % c == 0:
        print(number, end=" ")
print()