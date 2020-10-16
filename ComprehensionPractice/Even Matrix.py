size = int(input())
matrix = [list(map(int, input().split(", "))) for i in range(size)]

print([[even_number for even_number in curr_list if even_number % 2 == 0] for curr_list in matrix])
