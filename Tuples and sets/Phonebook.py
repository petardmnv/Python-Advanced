data = list(input().split("-"))
my_phonebook = {}
while True:
    if len(data) == 2:
        if data[0] not in my_phonebook.keys():
            my_phonebook[data[0]] = 0
        my_phonebook[data[0]] = data[1]
        data = list(input().split("-"))
    else:
        for i in range(int(data[0])):
            name = input()
            if name in my_phonebook.keys():
                print(f"{name} -> {my_phonebook[name]}")
            else:
                print(f"Contact {name} does not exist.")
        break
