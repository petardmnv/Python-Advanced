words = input().split(", ")

my_dict = {word: len(word) for word in words}
i = 0
for items in my_dict.items():
    if i == 0:
        print(f'{items[0]} -> {items[1]}', end="")
    else:
        print(f', {items[0]} -> {items[1]}', end="")
    i += 1
