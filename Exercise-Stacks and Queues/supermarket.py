from collections import deque
queue = deque()
while True:
    comand = input()
    if comand == 'End':
        print(f"{queue.__len__()} people remaining.")
        break
    elif comand == 'Paid':
        while len(queue):
            print(queue.popleft())
    else:
        queue.append(comand)
