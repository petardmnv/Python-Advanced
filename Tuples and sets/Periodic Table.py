lines = int(input())
chemicals = set()

for i in range(lines):
    name = input().split(" ")
    for i in range(len(name)):
        chemicals.add(name[i])

for chemical in chemicals:
    print(chemical)