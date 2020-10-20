my_list = list(map(int, input().split(", ")))

positive_nums = [num for num in my_list if num >= 0]
negative_nums = [num for num in my_list if num not in positive_nums]
even = [num for num in my_list if num % 2 == 0]
odd = [num for num in my_list if num not in even]

print(f'Positive: {", ".join(map(str, positive_nums))}')
print(f'Negative: {", ".join(map(str, negative_nums))}')
print(f'Even: {", ".join(map(str, even))}')
print(f'Odd: {", ".join(map(str, odd))}')
