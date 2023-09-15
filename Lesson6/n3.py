import random
from modules import validate_queens
# def validate_queens(queens):
#     for i in range (len(queens)):
#         for j in range(i+1, len(queens)):
#             if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0]-queens[j][0]) == abs(queens[i][1] - queens[j][1]):
#                 return False
#     return True

def generate_positions():
    for i in range(4):
        queens = []
        while queens == [] or not validate_queens(queens):  # если расстановка не успешная, перемешиваем ещё раз
            queens = []
            for row in range (1,9):
                col = random.randint(1,8)
                queen = [row, col]
                queens.append(queen)
        print(f'Набор координат номер {i+1}: {queens}')

generate_positions()
