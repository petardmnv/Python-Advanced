heroes = input().split(", ")

inventory = {name: dict() for name in heroes}
data = input()
while data != "End":
    curr_cost = 0
    h_name, h_item, h_cost = data.split("-")
    h_cost = int(h_cost)
    if h_item not in inventory[h_name]:
        inventory[h_name][h_item] = h_cost

    data = input()

[print(f'{name} -> Items: {len(inventory[name])}, Cost: {sum(inventory[name].values())}') for name in heroes]
