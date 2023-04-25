a, b = map(int, input().split())
word = list()
for _ in range(a):
    inp = input()
    if len(inp) >= b:
        word.append(inp)
word.sort(key=lambda x: )
print(word)