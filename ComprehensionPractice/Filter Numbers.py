first = int(input())
second = int(input())
print([num for num in range(first, second + 1) if any([num % i == 0 for i in range(2, 11)])])


