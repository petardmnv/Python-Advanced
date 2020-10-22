from itertools import permutations
string = list(input())
result = list((permutations(string, len(string))))
for word in result:
    for seq in word:
        print(seq, end="")
    print()