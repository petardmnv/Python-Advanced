from collections import  deque
eff = deque(map(int, input().split(", ")))
cas = list(map(int, input().split(", ")))

d_b = 0
c_b = 0
s_b = 0
is_fill = False

while len(cas) > 0 and len(eff) > 0:
    if d_b >= 3 and s_b >= 3 and c_b >= 3:
        is_fill = True
        break
    bomb_ef = eff.popleft()
    bomb_ca = cas.pop()
    is_created = False
    if bomb_ca + bomb_ef == 40:
        d_b += 1
        is_created = True
    elif bomb_ca + bomb_ef == 60:
        c_b += 1
        is_created = True
    elif bomb_ca + bomb_ef == 120:
        s_b += 1
        is_created = True
    if not is_created and bomb_ef + bomb_ca > 40:
        eff.appendleft(bomb_ef)
        cas.append(bomb_ca - 5)
    if bomb_ca + bomb_ef < 40:
        eff.appendleft(bomb_ef)

if is_fill:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if len(eff) > 0:
    print(f"Bomb Effects: ", end="")
    print(", ".join(map(str, eff)))
else:
    print("Bomb Effects: empty")
if len(cas) > 0:
    print(f"Bomb Casings: ", end="")
    print(", ".join(map(str, cas)))
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {c_b}")
print(f"Datura Bombs: {d_b}")
print(f"Smoke Decoy Bombs: {s_b}")



