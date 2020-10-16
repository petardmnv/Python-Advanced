size = int(input())
matrix = [list(map(int, input().split(", "))) for i in range(size)]

print([number for line in matrix for number in line])
