box = list(map(lambda x: int(x), input().split(" ")))
rack_size = int(input())
rack = rack_size
racks_used = 1
while box:
    value = box.pop()
    if rack > value:
        rack -= value
    elif rack == value:
        rack = rack_size
        if len(box) > 0:
            racks_used += 1
    else:
        box.append(value)
        rack = rack_size
        racks_used += 1
print(racks_used)
