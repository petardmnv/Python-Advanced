my_list = list(map(int, input().split(", ")))

possitive_nums = [num for num in my_list if num >= 0]
negative_nums = [num for num in my_list if num < 0]
even = [num for num in my_list if num % 2 == 0]
odd = [num for num in my_list if num % 2 != 0]

print(f'Possitive: {", ".join(map(str, possitive_nums))}')
print(f'Negative: {", ".join(map(str, negative_nums))}')
print(f'Even: {", ".join(map(str, even))}')
print(f'Odd: {", ".join(map(str, odd))}')
