strings = input().split(" ")

result = [word for word in strings if len(word) % 2 == 0]
for i in result:
    print(i)
