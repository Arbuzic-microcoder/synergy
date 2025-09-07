import random

# Размер матрицы
n = 10

# Создание первой матрицы с случайными числами от -50 до 50
matrix1 = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(-50, 50))
    matrix1.append(row)

# Создание второй матрицы с случайными числами от -50 до 50
matrix2 = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(-50, 50))
    matrix2.append(row)

# Сложение двух матриц
matrix_sum = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix1[i][j] + matrix2[i][j])
    matrix_sum.append(row)

# Вывод результатов
print("Матрица 1:")
for row in matrix1:
    print(row)

print("\nМатрица 2:")
for row in matrix2:
    print(row)

print("\nСумма матриц:")
for row in matrix_sum:
    print(row)