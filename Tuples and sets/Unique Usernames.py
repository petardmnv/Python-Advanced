lines = int(input())
usernames = set()

for i in range(lines):
    name = input()
    usernames.add(name)

for username in usernames:
    print(username)