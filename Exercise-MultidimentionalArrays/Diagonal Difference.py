size = int(input())

matrix = [[0] * size for row in range(size)]

for row in range(size):
    line = list(map(int, input().split()))
    for column in range(size):
        matrix[row][column] = line[column]
diagonal_1 = 0
diagonal_2 = 0

diagonal_1 = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
diagonal_2 = sum(matrix[i][size - i - 1] for i in range(size))

print(abs(diagonal_2 - diagonal_1))
