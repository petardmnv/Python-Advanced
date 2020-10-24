matrix = [["a" for j in range(8)] for i in range(8)]

result = []
for i in range(8):
    my_l = input().split(" ")
    for j in range(8):
        matrix[i][j] = my_l[j]

k_r = 0
k_c = 0
for i in range(8):
    if matrix[i].__contains__("K"):
        k_c = matrix[i].index("K")
        k_r = i
def find_queen(matrix):
    res = []
    for i in range(8):
        if matrix[i].__contains__("Q"):
            res.append(i)
            res.append(matrix[i].index("Q"))
            return res
    return [-1, -1]
#(x+1, y): one step horizontal move to the right.
#(x-1, y): one step horizontal move to the left.
#(x+1, y+1): one step diagonal move up-right.
#(x-1, y-1): one step diagonal move down-left.
#(x-1, y+1): one step diagonal move left-up.
#(x+1, y-1): one step diagonal move right-down.
#(x, y+1): one step downward.
#(x, y-1): one step upward.

def q_moves(matrix, x, y):
    moves = []
    moves.append(["x+i", "y"])
    moves.append(["x-i", "y"])
    moves.append(["x+i", "y+i"])
    moves.append(["x-i", "y-i"])
    moves.append(["x-i", "y+i"])
    moves.append(["x+i", "y-i"])
    moves.append(["x", "y+i"])
    moves.append(["x", "y-i"])
    for m in moves:
        for i in range(1, 8):
            r = eval(m[0])
            c = eval(m[1])
            if r < 0 or r > 7 or c < 0 or c > 7:
                break
            elif matrix[r][c] == "Q" or matrix[r][c] == "q":
                break
            elif r == k_r and c == k_c:
                return [x, y]
    return [-2, -2]


while find_queen(matrix)[0] != -1:
    curr_ind_1 = q_moves(matrix, find_queen(matrix)[0], find_queen(matrix)[1])[0]
    curr_ind_2 = q_moves(matrix, find_queen(matrix)[0], find_queen(matrix)[1])[1]
    if curr_ind_1 != -2 and curr_ind_2 != -2:
        result.append([curr_ind_1, curr_ind_2])
    matrix[find_queen(matrix)[0]][find_queen(matrix)[1]] = "q"

if len(result) == 0:
    print("The king is safe!")
else:
    [print(re) for re in result]




