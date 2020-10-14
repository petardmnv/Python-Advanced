sizes = list(map(int, input().split(", ")))
rows = sizes[0]
columns = sizes[1]

matrix = [[0] * columns for row in range(rows)]
for row in range(rows):
    line = list(map(int, input().split(", ")))
    for column in range(columns):
        matrix[row][column] = line[column]
summed = [0] * columns
for column in range(columns):
    for row in range(rows):
        summed[column] += matrix[row][column]
    print(summed[column])
