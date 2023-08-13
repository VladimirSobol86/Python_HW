import fractions

a = str(input("Введите дробь в виде a/b: "))
b = str(input("Введите дробь в виде a/b: "))
print("--------------------------------")

num1_a, num2_a = map(int, a.split("/"))
num1_b, num2_b = map(int, b.split("/"))

#Вычисление суммы дробей
num1_sum = num1_a * num2_b + num1_b * num2_a
num2_sum = num2_a * num2_b
#Переменные для цикла while
num1_for_divider = num1_sum
num2_for_divider = num2_sum
#Наибольший общий делитель для числителя и знаменателя суммы
while num1_for_divider != 0 and num2_for_divider != 0:
    if num1_for_divider > num2_for_divider:
        num1_for_divider %= num2_for_divider
    else:
        num2_for_divider %= num1_for_divider
max_divider_sum = num1_for_divider + num2_for_divider
print(f'Сумма дробей: {num1_sum}/{num2_sum}')
print("Наибольший общий делитель для суммы дробей: ", max_divider_sum)
print(f'Сумма дробей после сокращения: {num1_sum//max_divider_sum}/{num2_sum//max_divider_sum}')
print("--------------------------------")

#Вычисление произведения дробей
num1_prod = num1_a * num1_b
num2_prod = num2_a * num2_b
#Переменные для цикла while
num1_for_divider2 = num1_prod
num2_for_divider2 = num2_prod
#Наибольший общий делитель для числителя и знаменателя произведения
while num1_for_divider2 != 0 and num2_for_divider2 != 0:
    if num1_for_divider2 > num2_for_divider2:
        num1_for_divider2 %= num2_for_divider2
    else:
        num2_for_divider2 %= num1_for_divider2
max_divider_prod = num1_for_divider2 + num2_for_divider2
print(f'Произведение дробей: {num1_prod}/{num2_prod}')
print("Наибольший общий делитель для произведения дробей: ", max_divider_prod)
print(f'Произведение дробей после сокращения: {num1_prod//max_divider_prod}/{num2_prod//max_divider_prod}')
print("--------------------------------")

#Проверка
f1 = fractions.Fraction(a)
f2 = fractions.Fraction(b)
print(f'Проверка суммы дробей: {f1 + f2}')
print(f'Проверка произведения дробей: {f1 * f2}')