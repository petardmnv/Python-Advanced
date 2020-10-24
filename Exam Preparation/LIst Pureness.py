from collections import deque
def best_list_pureness(*argv):
    my_l = deque(argv[0])
    result = []
    number = 0
    for j in range(len(my_l)):
        number += j * my_l[j]
    result.append(number)
    rotations = argv[1]
    for i in range(rotations):
        number = 0
        last = my_l.pop()
        my_l.appendleft(last)
        for j in range(len(my_l)):
            number += j * my_l[j]
        result.append(number)
    return f"Best pureness {max(result)} after {result.index(max(result))} rotations"





