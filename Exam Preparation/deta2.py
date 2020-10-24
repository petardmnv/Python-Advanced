matrix = [["a" for j in range(8)] for i in range(8)]

result = []
for i in range(8):
    my_l = input().split(" ")
    print(my_l)
    for j in range(8):
        matrix[i][j] = my_l[j]
for i in range(8):
    if matrix[i].__contains__("K"):
        c = matrix[i].index("K")
        r = i
        print(r, c)
        break
for n in

