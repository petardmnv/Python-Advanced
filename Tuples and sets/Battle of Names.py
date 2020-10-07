def print_set(my_set):
    while my_set:
        print(my_set.pop(), end="")
        if len(my_set) > 0:
            print(", ", end="")


lines = int(input())
odd_nums = set()
odd_sum = 0
even_nums = set()
even_sum = 0

for i in range(lines):
    name = input()
    asci_sum = 0
    for chara in name:
        asci_sum += ord(chara)
    asci_sum = int(asci_sum / (i + 1))
    if asci_sum % 2 == 0:
        even_nums.add(asci_sum)
        even_sum += asci_sum
    else:
        odd_nums.add(asci_sum)
        odd_sum += asci_sum

if odd_sum == even_sum:
    print_set(odd_nums | even_nums)
elif odd_sum > even_sum:
    print_set(odd_nums - even_nums)
else:
    print_set(odd_nums ^ even_nums)
