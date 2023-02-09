"""
Заполнить двумерный массив (12х10) "Змейкой" снизу вверх от 1 до 120, как показано на рисунке:
"""
# создание матрицы необходимой размерности
n, m = 12, 10
matrix = [[0] * m for _ in range(n)]

count = 1
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        matrix[i][j] = count
        count += 1
    if not i % 2:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(4), end=' ')
    print()