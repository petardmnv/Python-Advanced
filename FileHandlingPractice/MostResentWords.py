import re

with open("MyWords.txt") as words_f:
    words = words_f.read().split(" ")

with open("InputEx5") as text_f:
    text = text_f.read()

finder = {}

for word in words:
    pattern = rf'[\s-]({word})[\s.,?!]'
    matches = re.findall(pattern, text, re.MULTILINE + re.IGNORECASE)
    finder[word.lower()] = len(matches)

with open("output.txt", 'w') as f:
    for word, occ in sorted(finder.items(), key=lambda t: -t[1]):
        print(f'{word} - {occ}', file=f)


