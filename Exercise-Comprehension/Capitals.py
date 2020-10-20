dict_one = input().split(", ")
dict_two = input().split(", ")
countries_dict = {cou: cap for cou, cap in zip(dict_one, dict_two)}
[print(f'{cou} -> {cap}') for cou, cap in countries_dict.items()]


