sizes = list(map(int, input().split()))
rows = sizes[0]
columns = sizes[1]

matrix = [["", "", ""] for i in range(rows)]

for row in range(rows):
    line = list(input().split())
    for column in range(columns):
        matrix[row][column] = line[column]
command = input().split()
while command[0] != "END":
    if command[0] == "swap":
        if len(command) == 5:
            firstIndexRow = int(command[1])
            firstIndexCol = int(command[2])
            secondIndexRow = int(command[3])
            secondIndexCol = int(command[4])
            if firstIndexRow < rows and secondIndexRow < rows or firstIndexCol < columns and secondIndexCol < columns:
                matrix[firstIndexRow][firstIndexCol], matrix[secondIndexRow][secondIndexCol] = matrix[secondIndexRow][secondIndexCol], matrix[firstIndexRow][firstIndexCol]
                for row in range(rows):
                    for column in range(columns):
                        print(matrix[row][column], end=" ")
                    print()
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input().split()
