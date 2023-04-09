inp = int(input())
count = inp

for _ in range(inp):
    dan = input()
    for i in range(len(dan)-1):
        if dan[i] == dan[i+1]:
            continue
        elif dan[i] in dan[i + 1:]:
            count -= 1
            break
print(count)