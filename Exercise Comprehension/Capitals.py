dict_one = input().split(", ")
dict_two = input().split(", ")

[print(f'{cou} -> {cap}') for cou, cap in zip(dict_one, dict_two)]


