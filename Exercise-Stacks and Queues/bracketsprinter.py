text = input()
brackets = []
for i in range(len(text)):
    if text[i] == '(':
        brackets.append(i)
    elif text[i] == ')':
        index = brackets.pop();
        print(text[index: i + 1])
