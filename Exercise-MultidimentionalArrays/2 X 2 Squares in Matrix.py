sizes = list(map(int, input().split()))
rows = sizes[0]
columns = sizes[1]

equal_squares = 0

matrix = [["A"] * columns for row in range(rows)]
for row in range(rows):
    line = list(map(str, input().split()))
    for column in range(columns):
        matrix[row][column] = line[column]
for row in range(rows - 1):
    for column in range(columns - 1):
        is_equal = False
        if matrix[row][column] == matrix[row][column + 1] == matrix[row + 1][column] == matrix[row + 1][column + 1]:
            is_equal = True
        if is_equal:
            equal_squares += 1
print(equal_squares)