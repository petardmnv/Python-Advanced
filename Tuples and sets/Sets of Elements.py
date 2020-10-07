lenghts = list(map(lambda x: int(x), input().split(" ")))
first_set = set()
second_set = set()

for i in range(lenghts[0]):
    num = int(input())
    first_set.add(num)

for i in range(lenghts[1]):
    num = int(input())
    second_set.add(num)

for element in first_set & second_set:
    print(element)
