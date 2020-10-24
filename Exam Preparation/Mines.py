size = int(input())
bombs = int(input())
matrix = [[0 for j in range(size)] for i in range(size)]

def numering(c1, c2):
    number = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if ((c1 + i) < size) and ((c1 + i) >= 0) and ((c2 + j) < size) and ((c2 + j) >= 0):
                if matrix[c1 + i][c2 + j] == -1:
                    number += 1
    return number

for i in range(bombs):
    coordinates = input()
    coordinates = coordinates.replace("(", "").replace(")", "")
    my_cord = coordinates.split(", ")
    first = int(my_cord[0])
    second = int(my_cord[1])
    matrix[first][second] = -1

for row in range(size):
    for col in range(size):
        if matrix[row][col] != -1:
            matrix[row][col] = numering(row, col)
        print(matrix[row][col] if matrix[row][col] != -1 else "*", end=" ")
    print()

