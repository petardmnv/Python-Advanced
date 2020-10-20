from string import ascii_lowercase

size = list(map(int, input(). split(" ")))
rows = size[0]
columns = size[1]

def get_word (row, column):
    return f'{ascii_lowercase[row]}{ascii_lowercase[row + column]}{ascii_lowercase[row]}'


matrix = [[get_word(row, col) for col in range(columns)] for row in range(rows)]

for i in range(rows):
    print(" ".join(map(str, matrix[i])))
