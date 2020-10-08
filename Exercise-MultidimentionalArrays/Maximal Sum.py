sizes = list(map(int, input().split()))
rows = sizes[0]
columns = sizes[1]

matrix = [[0] * columns for i in range(rows)]

for row in range(rows):
    line = list(map(int, input().split()))
    for column in range(columns):
        matrix[row][column] = line[column]
maxSum = 0
maxMatrix = [[0] * 3 for i in range(3)]
for row in range(rows - 2):
    for column in range(columns - 2):
        tmpSum = 0
        tmpMatrix = [[0] * 3 for i in range(3)]
        for i in range(3):
            tmpSum += matrix[row + i][column] + matrix[row + i][column + 1] + matrix[row + i][column + 2]
            tmpMatrix[i][0] = matrix[row + i][column]
            tmpMatrix[i][1] = matrix[row + i][column + 1]
            tmpMatrix[i][2] = matrix[row + i][column + 2]
        if tmpSum > maxSum:
            maxSum = tmpSum
            for i in range(3):
                for j in range(3):
                    maxMatrix[i][j] = tmpMatrix[i][j]

print("Sum =", maxSum)
for i in range(3):
    print(maxMatrix[i][0], maxMatrix[i][1], maxMatrix[i][2], )

