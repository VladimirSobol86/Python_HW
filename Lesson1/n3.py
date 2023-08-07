from random import randint
LOWER_LIMIT, UPPER_LIMIT = 0, 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
#print("Загаданное число для проверки:", num)
user_try = 1
user_num = int(input("Введите число 0-1000: "))

while (user_num != num):
    if 0 > user_num:
        user_num = int(input("Значение меньше нуля! Попытка не будет засчитана. Введите число 0-1000: "))
    elif user_num > 1000:
        user_num = int(input("Значение больше 1000! Попытка не будет засчитана. Введите число 0-1000: "))
    else:
        if user_num < num:
            user_num = int(input(f"Ваше число меньше загаданного, попыток осталось {10-user_try}. Введите новое число 0-1000: "))
        else:
            user_num = int(input(f"Ваше число больше загаданного, попыток осталось {10-user_try}. Введите новое число 0-1000: "))
        user_try += 1
        if (user_try > 9) & (user_num != num):
            print ("У Вас закончились попытки :(")
            break
        elif (user_try > 9) & (user_num == num):
            print ("Поздравляю, Вы угадали число с последней попытки!")
            break
else:
    print(f"Поздравляю, Вы угадали число с {user_try} попытки!")