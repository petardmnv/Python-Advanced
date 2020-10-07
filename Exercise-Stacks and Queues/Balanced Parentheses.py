from collections import deque

brackets = deque(input())
sequence = []
result = True
while brackets:
    search = brackets.popleft()
    if search in "{([":
        sequence.append(search)
    else:
        if len(sequence) == 0:
            result = False
            break
        current_element = sequence.pop()
        if (current_element == "{" and search == "}") or(current_element == "[" and search == "]") or (current_element == "(" and search == ")"):
            pass
        else:
            result = False
            break
if result:
    print("YES")
else:
    print("NO")
