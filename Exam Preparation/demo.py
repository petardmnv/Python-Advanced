while find_queen(matrix)[0] >= 0:
    curr_ind_1 = q_moves(matrix, find_queen(matrix)[0], find_queen(matrix)[1])[0]
    curr_ind_2 = q_moves(matrix, find_queen(matrix)[0], find_queen(matrix)[1])[1]
    if curr_ind_1 == -2 and curr_ind_2 == -2:
        continue
    else:
        result.append([curr_ind_1, curr_ind_2])

[print(re) for re in result]








move = []
move.append(0)
move.append(1)
move.append(2)
move.append(3)
move.append(4)
move.append(5)
move.append(6)
move.append(7)
for i in move:
    is_ok = True
    while is_ok:
        if i == 0:
            for j in range(1, 8):
                if x + j < 0 or x + j > 7:
                    move.pop(0)
                    is_ok = False
                    break
                if matrix[x + j][y] == "Q":
                    is_ok = False
                    move.pop(0)
                    break
                elif matrix[x + j][y] == "K":
                    return [x + 1, y]
                else:
                    continue
        elif i == 1:
            for j in range(8):
                if x - j < 0 or x - j > 7:
                    move.pop(1)
                    break
                if matrix[x - j][y] == "Q":
                    move.pop(1)
                    break
                elif matrix[x - j][y] == "K":
                    return [x - 1, y]
        elif i == 2:
            for j in range(8):
                if x + j < 0 or x + j > 7 or y + j < 0 or y + j > 7:
                    move.pop(2)
                    break
                if matrix[x + j][y + j] == "Q":
                    move.pop(2)
                    break
                elif matrix[x + j][y + j] == "K":
                    return [x + j, y + j]
        elif i == 3:
            for j in range(8):
                if x - j < 0 or x - j > 7 or y - j < 0 or y - j > 7:
                    move.pop(3)
                    break
                if matrix[x - j][y - j] == "Q":
                    move.pop(3)
                    break
                elif matrix[x - j][y - j] == "K":
                    return [x - j, y - j]
        elif i == 4:
            for j in range(8):
                if x - j < 0 or x - j > 7 or y + j < 0 or y + j > 7:
                    move.pop(4)
                    break
                if matrix[x - j][y + j] == "Q":
                    move.pop(4)
                    break
                elif matrix[x - j][y + j] == "K":
                    return [x - j, y + j]
        elif i == 5:
            for j in range(8):
                if x + j < 0 or x + j > 7 or y - j < 0 or y - j > 7:
                    move.pop(5)
                    break
                if matrix[x + j][y - j] == "Q":
                    move.pop(5)
                    break
                elif matrix[x + j][y - j] == "K":
                    return [x + j, y - j]
        elif i == 6:
            for j in range(8):
                if y + j < 0 or y + j > 7:
                    move.pop(6)
                    break
                if matrix[x][y + j] == "Q":
                    move.pop(6)
                    break
                elif matrix[x][y + j] == "K":
                    return [x, y + j]
        elif i == 7:
            for j in range(8):
                if y - j < 0 or y - j > 7:
                    move.pop(7)
                    break
                if matrix[x][y - j] == "Q":
                    move.pop(7)
                    break
                elif matrix[x][y - j] == "K":
                    return [x, y - j]


