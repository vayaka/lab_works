from random import randint

try:
    n_lists = int(input("Введите кол-во элементов в массиве >> "))
except ValueError:
    print("Должно быть число....")
    n_lists = 10
    print("Установленно значение по умолчанию -> 10")

sides = [randint(0, 100) for i in range(n_lists)]
sides = sorted(sides, reverse=True)
smax = 0
for i in range(len(sides)):
    for j in range(i + 1, len(sides)):
        for k in range(j + 1, len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
            s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
            if s > smax:
                smax = s
print("Максимальная площадь треугольника", smax)
