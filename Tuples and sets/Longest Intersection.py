lines = int(input())
longest = []

for i in range(lines):
    sequence = list(input().split("-"))
    first_range = sequence[0].split(",")
    second_range = sequence[1].split(",")
    tmp_set_one = set(range(int(first_range[0]), int(first_range[1]) + 1))
    tmp_set_two = set(range(int(second_range[0]), int(second_range[1]) + 1))
    tmp_set_one = sorted(tmp_set_one & tmp_set_two)
    if len(tmp_set_one) >= len(longest):
        longest = tmp_set_one
print(f"Longest intersection is {longest} with length {len(longest)}")
