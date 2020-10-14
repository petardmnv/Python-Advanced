size = int(input())

horse_moves = (
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
    (2, 1),
    (-2, 1),
    (2, -1),
    (-2, -1)
)


def top_horse(battle_field, needed_size, max_deaths):
    for i in range(needed_size):
        for j in range(needed_size):
            if battle_field[i][j] == 'K':
                deaths = 0
                for move_by_r, move_by_c in horse_moves:
                    if ((i + move_by_r) < size) and ((j + move_by_c) < size) and ((j + move_by_c) >= 0) and \
                            ((i + move_by_r) >= 0):
                        if matrix[i + move_by_r][j + move_by_c] == matrix[i][j]:
                            deaths += 1
                if deaths > max_deaths[0]:
                    max_deaths[0] = deaths
                    max_deaths[1] = i
                    max_deaths[2] = j
    return max_deaths


def is_quiet(battle_field, needed_size):
    for i in range(needed_size):
        for j in range(needed_size):
            if battle_field[i][j] == 'K':
                for move_by_r, move_by_c in horse_moves:
                    if ((i + move_by_r) < size) and ((j + move_by_c) < size) and ((j + move_by_c) >= 0) and \
                            ((i + move_by_r) >= 0):
                        if matrix[i + move_by_r][j + move_by_c] == matrix[i][j]:
                            return False
    return True


matrix = [['0'] * size for row in range(size)]

for row in range(size):
    line = input()
    for column in range(size):
        if line[column] == 'K':
            matrix[row][column] = 'K'

killed_horses = 0
while not is_quiet(matrix, size):
    max_deaths = [0, 0, 0]
    matrix[top_horse(matrix, size, max_deaths)[1]][top_horse(matrix, size, max_deaths)[2]] = '0'
    killed_horses += 1

print(killed_horses)
#5

#0K0K0

#K000K

#00K00

#K000K

#0K0K0
