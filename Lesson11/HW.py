class Matrix:
    def __init__(self, matrix):
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")

        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для сложения размеры матриц должны совпадать")

        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")

        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)
    
m0 = Matrix([[1, 2, 3], [3, 4, 2], [1, 1, 3]])
m1 = Matrix([[1, 2, 3], [3, 4, 2], [1, 1, 3]])
m2 = Matrix([[2, 1, 3], [0, 1, 5], [1, 1, 9]])
m3 = Matrix([[1, 2, 3], [3, 4, 2], [1, 1, 3]])
# При запуске программы с раскоменченой m4, выдается ошибка о некорректных размерах матрицы
# m4 = Matrix([[1, 2, 3], [3, 4], [1, 1, 3]])
m5 = Matrix([[1, 2], [3, 4], [1, 1]])
m6 = Matrix([[1, 2, 3], [3, 4, 2], [1, 1, 3]])
#Положитльные проверки
print(f'Сравнение одинаковых матриц \n{m0 == m1}')
print(f'Сравнение матриц с разной длиной \n{m0 == m5}')
print(f'Сравнение матриц с одинаковой длиной \n{m0 == m2}')
print(f'Первая матрица \n{m1}')
print(f'Вторая матрица \n{m2}')
print(f'Сложение матриц \n{m1 + m2}')
print(f'Умножение матриц \n{m1 * m2}')
#Отрицательные проверки
#print(f'Сложение матриц с разными размерами \n{m5 + m6}')
#print(f'Сложение матриц с неравным количеством строк и столбцов \n{m5 * m6}')