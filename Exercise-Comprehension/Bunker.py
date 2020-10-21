categories = {category: list() for category in input().split(", ")}

quantity = 0
quality = 0

n = int(input())

for i in range(n):
    type = input().split(" - ")
    categories[type[0]].append(type[1])

    curr_quantity_st, curr_quality_st = type[2].split(";")
    curr_quantity = curr_quantity_st.split(":")
    curr_quality = curr_quality_st.split(":")

    quality += int(curr_quality[1])
    quantity += int(curr_quantity[1])


quality = quality / len(categories)

print(f'Count of items: {quantity}')
print(f'Average quality: {quality:.2f}')
[print(f'{key} -> {", ".join(categories[key])}') for key in categories.keys()]




