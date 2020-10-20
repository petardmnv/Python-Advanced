size = int(input())

matrix = [
    [num for num in map(int, input().split(", "))]
    for i in range(size)
]
f_diagonal = [matrix[i][i] for i in range(size)]
sum_1 = sum(f_diagonal)
s_diagonal = [matrix[i][size - i - 1] for i in range(size)]
sum_2 = sum(s_diagonal)

print(f'First diagonal: {", ".join(map(str, f_diagonal))}', end=". ")
print(f'Sum: {sum_1}')
print(f'Second diagonal: {", ".join(map(str, s_diagonal))}', end=". ")
print(f'Sum: {sum_2}')


