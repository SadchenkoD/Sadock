# Задание №3

import math

r1 = float(input("Введите R1: "))
r2 = float(input("Введите R2: "))
total = round(r1 + r2, 1)

print(f"Общее сопротивление: {total} Ом")

# Задание №5

import math
 
m = int(input("Введите количество минут: "))

print(f"Часов: {m // 60}")
print(f"Минут: {m % 60}")

# Задание №6

import math 

def solve_quadratic(a, b, c, m, n):
    
    discriminant = b**2 - 4*a*c #Дискриминант
    
    if discriminant < 0:    #Нет действительных корней 
        return False
    
    elif discriminant == 0:  #Один корень 
        x = -b / (2*a)
        return m <= x <= n
    
    else:
        sqrt_d = math.sqrt(discriminant) #Два корня 
        x1 = (-b - sqrt_d) / (2*a)
        x2 = (-b + sqrt_d) / (2*a)
        
        return (m <= x1 <= n) or (m <= x2 <= n)

print("Введите коэффициенты:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print("Введите границы отрезка:")
m = float(input("m = "))
n = float(input("n = "))

result = solve_quadratic(a, b, c, m, n) #Проверка и вывод результата 

if result:
    print("Решение попадает в отрезок [{}; {}]".format(m, n))
else:
    print("Решение НЕ попадает в отрезок [{}; {}]".format(m, n))
