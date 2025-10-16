# Задание 1.1
x = float(input("Введите вещественное число x: "))
if x >= 0:
    f = x + x**2
else:
    f = 1 / x
print(f"f({x}) = {f:.2f}")

# Задание 1.2
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))

if a != b:
    maximum = max(a, b)
    minimum = min(a, b)
    print(f"Максимальное число: {maximum}")
    print(f"Минимальное число: {minimum}")
else:
    print("Числа должны быть различными!")


