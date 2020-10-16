sizes = list(map(int, input().split(" ")))

matrix = [[i + 1 for i in range(sizes[1])] for j in range(sizes[0])]

print([[matrix[row][column] for column in range(sizes[1])] for row in range(sizes[0])])