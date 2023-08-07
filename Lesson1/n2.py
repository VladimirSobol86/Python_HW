num = int(input("Введите число: "))
count = 0

if (num < 0) | (num > 100000):
    print("Введено недопустимое число")
elif (num == 1) | (num == 0):
    print("Число не является простым или составным")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count <= 2:
        print("Простое число")
    else:
        print("Составное число")