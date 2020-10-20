sep_lists = input().split("|")

my_list = [i.split() for i in sep_lists]
[[print(my_list[i][j], end=" ") for j in range(len(my_list[i]))] for i in range(len(my_list) - 1, -1, -1)]

