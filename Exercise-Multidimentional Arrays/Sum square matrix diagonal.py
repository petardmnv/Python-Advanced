size = int(input())

matrix = [[0] * size for row in range(size)]

for row in range(size):
    line = list(map(int, input().split()))
    for column in range(size):
        matrix[row][column] = line[column]
sum_diagonal = 0
for diagonal_index in range(size):
    sum_diagonal += matrix[diagonal_index][diagonal_index]
print(sum_diagonal)

