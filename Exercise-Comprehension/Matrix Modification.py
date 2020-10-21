size = int(input())

matrix = [list(map(int, input().split(" "))) for i in range(size)]

def are_valid(row, column):
    if row >= size or column >= size or row < 0 or column < 0:
        return False
    return True


command = input()
while command != 'END':
    commands = command.split(" ")
    row = int(commands[1])
    column = int(commands[2])
    number = int(commands[3])
    if commands[0] == "Add":
        if are_valid(row, column):
            matrix[row][column] += number
        else:
            print("Invalid coordinates")

    elif commands[0] == 'Subtract':
        if are_valid(row, column):
            matrix[row][column] -= number
        else:
            print("Invalid coordinates")

    command = input()

[print(" ".join(map(str, matrix[i]))) for i in range(size)]
