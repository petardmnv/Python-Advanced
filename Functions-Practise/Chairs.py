from itertools import permutations, combinations
string = list(input().split(", "))
ind = int(input())
result = list(combinations(string, ind))
for word in result:
    print(", ".join(word))