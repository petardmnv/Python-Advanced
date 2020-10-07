from collections import deque
pumps = int(input())

my_deque = deque()
best_index = -1
my_fuel = 0
for i in range(pumps):
    data = input().split(" ")
    fuel = int(data[0])
    km = int(data[1])
    my_fuel += fuel
    if my_fuel >= km:
        if best_index == -1:
            best_index = i
        my_fuel -= km
    else:
        my_fuel = 0
        best_index = -1

print(best_index)
