f = open("SumOfLines.txt")
sumLines = 0
for line in f:
    num = int(line.strip())
    sumLines += num
print(sumLines)
# print(sum([int(line.strip())for line in open("SumOfLines.txt")]))
f.close()