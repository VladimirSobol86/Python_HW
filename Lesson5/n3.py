def fibonacci(end):
    a, b = 0, 1
    while end > 0:
        yield a
        a, b = b, a + b
        end -= 1

count = int(input('Введите количество жеалемых чисел Фибоначчи: '))
for num in fibonacci(count):
    print(num)