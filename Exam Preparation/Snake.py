size = int(input())

matrix = [[" ", " ", " "]for i in range(size)]
apples = 0
crashed = False

curr_r = 0
curr_c = 0
matrix = [["a" for j in range(size)] for i in range(size)]
for i in range(size):
    my_l = input()
    for j in range(size):
        matrix[i][j] = my_l[j]
for i in range(size):
    for j in range(size):
        if matrix[i][j] == "S":
            curr_c = j
            curr_r = i
matrix[curr_r][curr_c] = "."
while apples < 10:
    comand = input()
    tpm_1 = curr_r
    tmp_2 = curr_c
    if comand == "left":
        curr_c -= 1
    elif comand == "right":
        curr_c += 1
    elif comand == "down":
        curr_r += 1
    elif comand == "up":
        curr_r -= 1
    if curr_r >= size or curr_r < 0 or curr_c >= size or curr_c < 0:
        crashed = True
        matrix[tpm_1][tmp_2] = "."
        break
    if matrix[curr_r][curr_c] == "B":
        matrix[curr_r][curr_c] = "."
        i = 0
        j = 0
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == "B":
                    if i != curr_r:
                        curr_c, curr_r = j, i
        matrix[curr_r][curr_c] = "."
    elif matrix[curr_r][curr_c] == "*":
        apples += 1
    matrix[curr_r][curr_c] = "."


if crashed:
    print("Game over!")
else:
    print("You won! You fed the snake.")
    matrix[curr_r][curr_c] = "S"

print(f"Food eaten: {apples}")
[print("".join(map(str, row))) for row in matrix]





