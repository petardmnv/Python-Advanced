text = str(input())
my_dict = {}
for i in text:
    if i not in my_dict.keys():
        my_dict[i] = 0
    my_dict[i] += 1

for key in sorted(my_dict):
    print(f"{key}: {my_dict[key]} time/s")
