def validate_queens(queens):
    for i in range (len(queens)):
        for j in range(i+1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0]-queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

#для успешной проверки
#queens = [[1, 7], [2, 4], [3, 2], [4, 8], [5, 6], [6, 1], [7, 3], [8, 5]]
queens = []
for _ in range(8):
    queen = list(map(int, input(f'Введите 2 координаты {_+1}-ой фигуры: ').split()))
    queens.append(queen)
print(queens)
if validate_queens(queens):
    print('Не бьют')
else:
    print('Бьют')