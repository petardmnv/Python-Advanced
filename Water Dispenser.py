from collections import deque

liters = int(input())

queue = deque()

while True:
    name = input()
    if name == "Start":
        break
    else:
        queue.append(name)

while True:
    command = input().split(" ")
    if command[0] == "End":
        print(f"{liters} liters left")
        break
    elif command[0] == "refill":
        liters += int(command[1])
    else:
        liters_needed = int(command[0])
        if liters_needed <= liters:
            print(f"{queue.popleft()} got water")
            liters -= liters_needed
        else:
            print(f"{queue.popleft()} must wait")

