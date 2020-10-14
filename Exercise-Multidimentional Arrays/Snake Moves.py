sizes = list(map(int, input().split()))
rows = sizes[0]
columns = sizes[1]

snake = input()
snake_index = 0

matrix = [['0'] * columns for i in range(rows)]

for row in range(rows):
    if (row + 1) % 2 != 0:
        for column in range(columns):
            if snake_index == len(snake):
                snake_index = 0
            matrix[row][column] = snake[snake_index]
            snake_index += 1
    else:
        curr_m_index = columns - 1
        while curr_m_index >= 0:
            if snake_index == len(snake):
                snake_index = 0
            matrix[row][curr_m_index] = snake[snake_index]
            snake_index += 1
            curr_m_index -= 1

for row in range(rows):
    print("".join(matrix[row]))
