from itertools import permutations, chain

strings = list(input().split(", "))

length = len(strings)

exx = set(permutations("+" * length + "-" * length, length))

for ex in exx:
    result = "".join(list(chain(*zip(ex, strings))))
    print(f'{result}={eval(result)}')
